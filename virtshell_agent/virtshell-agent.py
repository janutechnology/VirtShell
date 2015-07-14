#!/usr/bin/python

""" Filename: VirtShell-agent
    Description: Agent for handle containers and virtual machines in a host
    moduleauthor: Carlos Alberto Llano R. <carlos_llano@hotmail.com> 
"""

__version__ = '1.0.0'

import simplejson
import datetime
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from logging.handlers import SysLogHandler

################################################################################
# Global Variables
################################################################################
main_logger = None

################################################################################
# CreateInstanceHandler Class
################################################################################
class CreateInstanceHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        main_logger.info("new connection")
        self.write_message("Connection stablished")
        CreateInstanceHandler.clients.append(self)

    def on_message(self, json_message):
        main_logger.info("message received %s" % json_message)
        message = simplejson.loads(json_message)

        instance = InstanceFactory.create_instance(message['type'])

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

class Instance(object):
    def __init__(self):
        self._price = None

    def create_instance(self):
        return self._price

class VirtualMachine(Instance):
    def __init__(self):
        self._price = 8.5

class Container(Instance):
    def __init__(self):
        self._price = 10.5

class InstanceFactory(object):
    @staticmethod
    def create_instance(instance_type):
        if instance_type == 'vmachine':
            return VirtualMachine()
        elif instance_type == 'container':
            return Container()

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
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()
    main_logger.info("VirtShell-agent started...")