import json
import time
import logging
import threading
from database import Database
#from exceptions import PluginException
from logging.handlers import SysLogHandler

def catalogue():
    return ['create', 'start', 'stop']

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

logger = init_logger('lxc-container')
database = Database(logger)

def create(request):        
    try:
        database.insert_new_request(request)
        create_daemon = threading.Thread(name = 'create_daemon',
                                         args = (request,),
                                         target = _create_container)
        create_container_thread.setDaemon(True)
        create_container_thread.start()
    except Exception as err:
        message_error = "Failed to create the container, %s" % err
        logger.error(message_error)
        request.status = 2
        request.message_log = message_error
        database.update_request(request)
        #raise PluginException(message_error)
    return request

def start(request):
    try:
        name = request.message['name']
        logger.info("starting container %s", name)
        subprocess.call(["lxc-start", 
                         "-n", 
                         name])
        logger.info("container %s started successfully." % name)
        request.message_log += "container started successfully\n"
        time.sleep(10)
    except Exception as err:
        message_error = "Failed to start the container, %s" % err
        logger.error(message_error)
        #raise PluginException(message_error)
    return request

def stop(request):
    try:
        name = request.message['name']
        logger.info("stoping container %s", name)
        subprocess.call(["lxc-stop", 
                         "-n", 
                         name])
        logger.info("container %s stoped successfully." % name)
        request.message_log += "container stoped successfully\n"
        time.sleep(10)
    except Exception as err:
        message_error = "Failed to stop the container, %s" % err
        logger.error(message_error)
        #raise PluginException(message_error)
    return request

def _create_container(request):
    try:
        request = database.get_request()
        while request != None:
            name = request.message['name']
            distribution = request.message['distribution']
            release = request.message['release']
            arch = request.message['arch']
            user = request.message['user']
            password = request.message['password']

            message_log = "creating container %s", name
            request.status = 1
            request.message_log = message_log
            database.update_request(request)

            logger.info(message_log)
            subprocess.call(["lxc-create",
                             "-t",
                             "download",
                             "-n",
                             name,
                             "--",
                             "--dist",
                             distribution,
                             "--release",
                             release,
                             "--arch",
                             arch])
            logger.info("container %s created successfully." % name)
            request.message_log += "container created successfully\n"
            request = start(request)
            request = _install_openssh_server(request)
            request = _create_user(request)
            
            # Next container 
            request = database.get_request()
    except Exception as err:
        message_error = "Failed to create the container, %s" % err
        logger.error(message_error)
        request.status = 2
        request.message_log = message_error
        database.update_request(request)

def _install_openssh_server(request):
    try:
        name = request.message['name']
        logger.info("[lxc_container] installing openssh-server \
                          in container %s" % name)
        subprocess.call(["lxc-attach", 
                         "-n", 
                         name,
                         "--",
                         "apt-get",
                         "install",
                         "-y",
                         "openssh-server"])
        logger.info("[lxc_container] openssh-server installed \
                          successfully in container %s" % name)
        request.message_log += "openssh-server installed successfully\n"
    except Exception as err:
        message_error = "[lxc_container] Error: Failed to install \
                         openssh-server in container, %s" % err
        logger.error(message_error)
        #raise PluginException(message_error)
    return request

def _create_user(request):
    try:
        name = request.message['name']
        user = request.message['user']
        password = request.message['password']
        logger.info("[lxc_container] creating user in \
                       container %s" % name)
        path = "/var/lib/lxc/%s/rootfs/" % name
        subprocess.call(["chroot",
                         path,
                         name, 
                         user, 
                         password,
                         "useradd",
                         "--create-home", 
                         "-s", 
                         "/bin/bash",
                         user])
        user_password = "\"" + user + ":" + password + "\""
        cmd = "echo \"%s:%s\" | sudo chroot %s chpasswd" % (user,
                                                         password,
                                                         path)
        subprocess.Popen(cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.STDOUT)
        logger.info("[lxc_container] user %s created successfully \
                       in container %s" % (user,name))
        request.message_log += "user %s created successfully\n" % user
    except Exception as err:
        message_error = "[lxc_container] Error: Failed to create the \
                       user %s in container %s, %s" % (user, name, err)
        logger.error(message_error)
        #raise PluginException(message_error)
    return request