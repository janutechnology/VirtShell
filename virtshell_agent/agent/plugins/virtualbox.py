import json
import time
import logging
from exceptions import PluginException
from logging.handlers import SysLogHandler

def catalogue():
    return ['create'] 

def init_logger(LoggerName):
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

logger = init_logger('virtualbox')    

def create(request, logge):
    try:
        request = _register(request)
        request = _modify(request)
    except Exception as err:
        message_error = "[virtualbox] Error: Failed to create the \
                         machine, %s" % err
        logger.error(message_error)
        raise PluginException(message_error)
    return request            

def _register(name, distribution, arch):
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
        logger.error(message_error)
        raise PluginException(message_error)
    return request

def _modify(request):
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
        logger.error(message_error)
        raise PluginException(message_error)
    return request    