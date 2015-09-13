import json
import time
import subprocess
from exceptions import PluginException

class VirtualBox(object):
    def __init__(self, logger):
        self.logger = logger

    def create(self, request):
        try:
            request = self._register(request)
            request = self._modify(request)
        except Exception as err:
            message_error = "[virtualbox] Error: Failed to create the \
                             machine, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request            

    def _register(self, name, distribution, arch):
        try:
            name = request.message['name']
            distribution = request.message['distribution']
            arch = request.message['arch']
            logger.info("[virtualbox] registering machine %s", request.message['name'])
            if '64' in request.message['arch']:
                ostype = request.message['distribution'].titel() + '_64'
            else:
                ostype = request.message['distribution'].titel()
            subprocess.call(["VBoxManage", 
                             "createvm", 
                             "--name", 
                             request.message['name'],
                             "--ostype",
                             ostype,
                             "--register"])
            logger.info("[virtualbox] machine %s registered successfully." % 
                                                                        name)
            request.message_log += "machine registered successfully\n"
        except Exception as err:
            message_error = "[virtualbox] Error: Failed to register \
                             the machine, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

    def _modify(self, request):
        try:
            name = request.message['name']
            memory = request.message['memory']
            cpus = request.message['cpus']
            logger.info("[virtualbox] assigning the properties of \
                         the machine %s", name)
            subprocess.call(["VBoxManage", 
                             "modifyvm", 
                             "--name", 
                             request.message['name'],
                             "--memory",
                             request.message['memory'],
                             "--cpus",
                             cpus,
                             request.message['cpus'], 
                             "on",
                             "--bridgeadapter1",
                             "eth0",
                             "--nic1",
                             "bridged"])
            logger.info("[virtualbox] properties of machine %s assigned \
                         successfully." % name)
            request.message_log += "machine's properties assigned successfully\n"            
        except Exception as err:
            message_error = "[virtualbox] Error: Failed to register \
                             the machine, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request      

def run(logger, request):
    virtualbox = VirtualBox(logger)
    action = request.message['action']
    if action == 'create':
        return virtualbox.create(request)
    elif action == 'start':
        return virtualbox.start(request)      