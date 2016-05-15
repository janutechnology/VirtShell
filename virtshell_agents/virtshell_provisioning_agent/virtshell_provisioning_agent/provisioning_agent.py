""" Filename: provisioning_agent
    Description: Agent to provisioning containers and virtual machines in a host
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
import logger
import os.path
import datetime
import threading
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver

################################################################################
# Global Variables
################################################################################
main_logger = None
listener_handler = None

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
class ListenerHandler(object):
    def __init__(self):
        self.listeners = {}
        self.plugins = {}
        self.plugin_folder = "./plugins"
        self.special_method = "__init__.py"
        self.get_plugins()
        self.register_plugin_actions()

    def register_plugin_actions(self):
        for plugin_name in self.plugins:
            plugin_class = self.load_plugin(plugin_name)
            plugin_methods = plugin_class.catalogue()
            for plugin_method_name in plugin_methods:
                plugin_method = getattr(plugin_class, plugin_method_name)
                plugin_key = plugin_class.driver() + '-' + plugin_method_name
                self.register(plugin_key, (plugin_class, plugin_method))

    def register(self, action, listener):
        self.listeners[action] = listener
        main_logger.info("action registered: " + action + " listener: " + str(listener))

    def dispatch(self, request):
        message = json.loads(request)
        action = message['driver'] + '-' + message['action']
        plugin, method = self.listeners[action]
        main_logger.info("dispatch action: " + action + " plugin: " + str(plugin) + " method: " + str(method))
        create_daemon = threading.Thread(name = 'create_daemon',
                                         args = (request,),
                                         target = method)
        create_daemon.setDaemon(True)
        create_daemon.start()
            
    def get_plugins(self):
        main_logger.info("finding plugins")
        possible_plugins = os.listdir(self.plugin_folder)
        possible_plugins.remove(self.special_method)
        for module in possible_plugins:
            if not module.endswith(".pyc") and not os.path.isdir(module):
                module = os.path.splitext(module)[0]
                info = imp.find_module(module, [self.plugin_folder])
                self.plugins[module] = info
                main_logger.info("plugin %s.py found" % module)

    def load_plugin(self, name):
        main_logger.info("loading plugin " + name)
        return imp.load_module(name, *(self.plugins[name]))

################################################################################
# RequestHandler Class
################################################################################
class RequestHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        main_logger.info("New connection stablished")
        RequestHandler.clients.append(self)

    def on_message(self, json_message):
        main_logger.info("message received %s" % json_message)
        listener_handler.dispatch(json_message)
        self.write_message(u"received")

    def on_close(self):
        main_logger.info("connection closed")
        RequestHandler.clients.remove(self)

application = tornado.web.Application([(r'/', RequestHandler)])

if __name__ == "__main__":
    main_logger = logger.get_logger('virtshell-provisioning-agent')
    listener_handler = ListenerHandler()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    main_logger.info("agent started...")
    #tornado.ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=15), WSHandler.write_to_clients)
    tornado.ioloop.IOLoop.instance().start()