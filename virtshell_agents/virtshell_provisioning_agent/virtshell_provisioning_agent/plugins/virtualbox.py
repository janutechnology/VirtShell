import json
import time
import config
import logging
import requests
from database import Database
#from exceptions import PluginException
from logging.handlers import SysLogHandler

def catalogue():
    return ['create']

def driver():
    return "virtualbox" 

def init_logger(LoggerName):
    # Create logger
    logger = logging.getLogger(LoggerName)
    logger.setLevel(logging.INFO)

    handler = logging.handlers.SysLogHandler(address='/dev/log')

    handler.setLevel(logging.INFO)
    # Create formatter
    formatter = logging.Formatter('%(asctime)s %(name)s '
                                  '%(levelname)s %(message)s')
    # Add formatter and handler
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger  

logger = init_logger('virtualbox-plugin')
database = Database(logger)

def create(request):
    request_id = database.insert_new_request(request)
    request_json = json.loads(request)
    request_json['id'] = request_id

    try:
        request = _register(request_json)
        #request = _modify(request)
    except Exception as err:
        message_error = "[virtualbox] Error: Failed to create the machine, %s, reason: %s" % (request_json['name'], err)
        logger.error(message_error)
    return request

def _update_task(uuid, state , log):
    url = "%s/tasks/%s" % (config.VIRTSHELL_SERVER, uuid)
    r = requests.put(url, data = json.dumps({'status': state, 'log': log}))           

def _register(request_json):
    try:
        name = request_json['name']
        distribution = request_json['distribution']
        arch = request_json['arch']

        _update_task(request_json['task_uuid'],
                     "registering", 
                     "virtualbox_plugin")

        logger.info("[virtualbox] registering virtual machine " + name)

        if '64' in request_json['arch']:
            ostype = request_json['distribution'].title() + '_64'
        else:
            ostype = request_json['distribution'].title()

        subprocess.call(["VBoxManage", 
                         "createvm", 
                         "--name", 
                         name,
                         "--ostype",
                         ostype,
                         "--register"])

        VBoxManage createvm --name testMachine --ostype Ubuntu_64 --register

        logger.info("[virtualbox] machine %s registered successfully." % name)

        _update_task(request_json['task_uuid'],
                      "registered", 
                      "virtualbox_plugin")

        request_json_log += "machine registered successfully\n"

    except Exception as err:
        message_error = "[virtualbox] Error: Failed to register the machine, %s, Reason:" % (name, err)
        logger.error(message_error)
    return request

def _modify(request):
    try:
        name = request_json['name']
        memory = request_json['memory']
        cpus = request_json['cpus']
        logger.info("[virtualbox] assigning the properties of \
                     the machine %s", name)

        subprocess.call(["VBoxManage", 
                         "modifyvm", 
                         "--name", 
                         request_json['name'],
                         "--memory",
                         request_json['memory'],
                         "--cpus",
                         cpus,
                         request_json['cpus'], 
                         "on",
                         "--bridgeadapter1",
                         "eth0",
                         "--nic1",
                         "bridged"])

        logger.info("[virtualbox] properties of machine %s assigned \
                     successfully." % name)

        request_json_log += "machine's properties assigned successfully\n"

    except Exception as err:
        message_error = "[virtualbox] Error: Failed to register \
                         the machine, %s" % err
        logger.error(message_error)
    return request    