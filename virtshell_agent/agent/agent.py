#!/usr/bin/python

""" Filename: agent
    Description: Agent for handle containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '0.1'

import os
import imp
import os.path
import logging
import datetime
import simplejson
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver
from logging.handlers import SysLogHandler
# from instance_factory import InstanceFactory

################################################################################
# Global Variables
################################################################################
main_logger = None
plugin_folder = "./plugins"
special_method = "__init__.py"
plugins = {}

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
        message = simplejson.loads(json_message)
        if message['action'] == 'create':
            plugin = load_plugin(message['type'])
            plugin.run()

    def on_close(self):
        main_logger.info("connection closed")
        CreateInstanceHandler.clients.remove(self)

    @classmethod
    def write_to_clients(cls):
        print "Writing to clients"
        for client in cls.clients:
            client.write_message("Hi there!")

application = tornado.web.Application([
  (r'/create_instance', CreateInstanceHandler)
])

################################################################################
# Functions for finding and loads plugins
################################################################################
def get_plugins():
    main_logger.info("finding plugins")
    possible_plugins = os.listdir(plugin_folder)
    possible_plugins.remove(special_method)
    for module in possible_plugins:
        if not module.endswith(".pyc"):
            module = os.path.splitext(module)[0]
            info = imp.find_module(module, [plugin_folder])
            plugins[module] = info
            main_logger.info("plugin %s.py found" % module)

def load_plugin(name):
    return imp.load_module(name, *(plugins[name]))

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
    get_plugins()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    main_logger.info("VirtShell-agent started...")
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
