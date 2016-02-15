import json
import time
import logging
import threading
from io import BytesIO
from docker import Client
from database import Database
from exceptions import PluginException
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

logger = init_logger('docker-container')
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
        raise PluginException(message_error)
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
        raise PluginException(message_error)
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
        raise PluginException(message_error)
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

            message_log = "creating docker-container %s", name
            request.status = 1
            request.message_log = message_log
            database.update_request(request)

            logger.info(message_log)

            client = Client(version='1.20', base_url='tcp://127.0.0.1:2376')

            distribution = "ubuntu:14.04"

            dockerfile = '''
            FROM ''' + distribution + '''
            MAINTAINER Carlos Llano <carlos_llano@hotmail.com>
            RUN sed 's/#$ModLoad imudp/$ModLoad imudp/' -i /etc/rsyslog.conf
            RUN sed 's/#$UDPServerRun 514/$UDPServerRun 514/' -i /etc/rsyslog.conf
            RUN sed 's/#$ModLoad imtcp/$ModLoad imtcp/' -i /etc/rsyslog.conf
            RUN sed 's/#$InputTCPServerRun 514/$InputTCPServerRun 514/' -i /etc/rsyslog.conf
            EXPOSE 514/tcp 514/udp 
            CMD ["/usr/sbin/rsyslogd", "-dn", "-f", "/etc/rsyslog.conf"]
            RUN apt-get install -y openssh-server
            RUN mkdir /var/run/sshd
            RUN useradd -s /bin/bash -m virtshell
            RUN echo "virtshell:virtshell" | chpasswd
            RUN echo "virtshell ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
            RUN echo "root:root" | chpasswd
            RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config
            RUN sed "s@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g" -i /etc/pam.d/sshd
            ENV NOTVISIBLE "in users profile"
            RUN echo "export VISIBLE=now" >> /etc/profile
            EXPOSE 22
            CMD ["/usr/sbin/sshd", "-D"]
            '''

            dockerfile_binary = BytesIO(dockerfile.encode('utf-8'))
            response = [line for line in client.build(fileobj=dockerfile_binary,
                                                      rm=True,
                                                      tag='ubuntu/15.04')]
            container = client.create_container(image='ubuntu:15.04')
            container_id = container['Id']

            client.start(container_id)
            link_path = client.inspect_container(container_id)
            ip = link_path['NetworkSettings']['IPAddress'])
            logger.info("docker-container %s created successfully." % name)
            request.message_log += "docker-container created successfully\n"
            request = start(request)
            request = _create_user(request)
            
            # Next container 
            request = database.get_request()
    except Exception as err:
        message_error = "Failed to create the container, %s" % err
        logger.error(message_error)
        request.status = 2
        request.message_log = message_error
        database.update_request(request)

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
        raise PluginException(message_error)
    return request