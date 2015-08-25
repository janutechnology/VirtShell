#!/usr/bin/python

""" Filename: agent
    Description: Agent for handle containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '0.1'

import os
import sys
import imp
import time
import json
import signal
import psutil
import os.path
import logging
import datetime
import tornado.web
import tornado.ioloop
import multiprocessing
import tornado.websocket
import tornado.httpserver
from database import Database
from logging.handlers import SysLogHandler

################################################################################
# Global Variables
################################################################################
main_logger = None
database = None

################################################################################
# Signals
################################################################################
def signal_handler(signal, frame):
    pid = os.getpid()
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        main_logger.info("agent-service with pid [%d] terminated.", child.pid)
        child.kill()
    main_logger.info("agent with pid [%d] terminated.", pid)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

################################################################################
# AgentService Class
################################################################################
class AgentService(multiprocessing.Process):
    def run(self):
        self.logger = init_logger('virtshell-agent-service')
        self.plugins = {}
        self.plugin_folder = "./plugins"
        self.special_method = "__init__.py"
        self.database = Database(self.logger)
        self.logger.info("started...")
        self.get_plugins()

        while True:
            request = self.database.get_request()
            if request != None:
                message = request.message
                plugin = self.load_plugin(message['type'])
                result = plugin.run(self.logger, message)
                if result == 0:
                    request.status = 1
                    self.database.update_request(request)
            else:
                time.sleep(10)
            self.logger.info("en el hilo....")
            
    def get_plugins(self):
        self.logger.info("finding plugins")
        possible_plugins = os.listdir(self.plugin_folder)
        possible_plugins.remove(self.special_method)
        for module in possible_plugins:
            if not module.endswith(".pyc"):
                module = os.path.splitext(module)[0]
                info = imp.find_module(module, [self.plugin_folder])
                self.plugins[module] = info
                self.logger.info("plugin %s.py found" % module)

    def load_plugin(self, name):
        return imp.load_module(name, *(self.plugins[name]))

################################################################################
# CreateInstanceHandler Class
################################################################################
class CreateInstanceHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        main_logger.info("new connection")
        main_logger.info("Connection stablished")
        CreateInstanceHandler.clients.append(self)

    def on_message(self, json_message):
        main_logger.info("message received %s" % json_message)
        #message = simplejson.loads(json_message)
        message = json.load(json_message)
        database.insert_new_request(message)
        self.write_message("received")

    def on_close(self):
        main_logger.info("connection closed")
        CreateInstanceHandler.clients.remove(self)

    @classmethod
    def write_to_clients(cls):
        for client in cls.clients:
            client.write_message("Hi there!")

application = tornado.web.Application([
  (r'/create_instance', CreateInstanceHandler)
])

################################################################################
# Logging plumbing
################################################################################
def init_logger(LoggerName):
    """ 
    This function handle the messages for SysLog
    
    @param LoggerName: The name of the logger

    @return: a logger instance
    """

    # Create logger
    logger = logging.getLogger(LoggerName)
    logger.setLevel(logging.INFO)
    # Create handler
    handler = SysLogHandler(address='/dev/log')
    handler.setLevel(logging.INFO)
    # Create formatter
    formatter = logging.Formatter('%(asctime)s %(name)s '
                                  '%(levelname)s %(message)s')
    # Add formatter and handler
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # Return logger
    return logger

if __name__ == "__main__":
    main_logger = init_logger('virtshell-agent')
    database = Database(main_logger)
    agent_service = AgentService()
    agent_service.start()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    main_logger.info("started...")
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
