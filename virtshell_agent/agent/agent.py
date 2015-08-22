#!/usr/bin/python

""" Filename: agent
    Description: Agent for handle containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '0.1'

import os
import imp
import signal
import os.path
import logging
import sqlite3
import datetime
import simplejson
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver
from database import Database
from logging.handlers import SysLogHandler

################################################################################
# Global Variables
################################################################################
main_logger = None
plugin_folder = "./plugins"
special_method = "__init__.py"
plugins = {}
database = None

################################################################################
# Signals
################################################################################
signals =  {
    signal.SIGINT: 'SIGINT',
    signal.SIGTERM: 'SIGTERM'
}

def cleanup(name, child, signum, frame):
    """Stop the sub-process *child* if *signum* is SIGTERM. Then terminate."""
    try:
        print('%s got a %s' % (name, SIGNALS[signum]))
        if child and signum != signal.SIGINT:
            term(child)
    except:
        traceback.print_exc()
    finally:
        sys.exit()

def term(proc):
    """Send a SIGTERM to *proc* and wait for it to terminate."""
    proc.terminate()  # Sends SIGTERM
    proc.wait()

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
        print message
        database.insert_new_request(message)
        # if message['action'] == 'create':
        #     plugin = load_plugin(message['type'])
        #     plugin.run()
        self.write_message("received")

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
    database = Database(main_logger)
    get_plugins()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    main_logger.info("VirtShell-agent started...")
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
