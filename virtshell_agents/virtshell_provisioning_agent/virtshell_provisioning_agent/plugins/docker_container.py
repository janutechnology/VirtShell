import json
import time
import config
import logging
import paramiko
import requests
from io import BytesIO
from docker import Client
from database import Database

def catalogue():
    return ['create', 'start', 'stop']

def driver():
    return 'docker'

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

logger = init_logger('docker-container-plugin')
database = Database(logger)

def create(request):
    request_id = database.insert_new_request(request)
    request_json = json.loads(request)
    request_json['id'] = request_id

    try:
        request_json = _create_container(request_json)
        _provisioning_container(request_json)
    except Exception as err:
        message_error = "Failed to create the container %s, reason: %s" % (request_json['name'], err)
        logger.error(message_error)
        request_json['status'] = 2
        request_json['message_log'] = message_error
        database.update_request(request_json)

def _update_task(uuid, state , log):
    url = "%s/tasks/%s" % (config.VIRTSHELL_SERVER, uuid)
    r = requests.put(url, data = json.dumps({'status': state, 'log': log}))

def _create_container(request_json):
    name = request_json['name']
    distribution = request_json['distribution']
    version = request_json['version']
    user = request_json['user']
    password = request_json['password']

    message_log = "docker_container_plugin creating docker-container %s... with %s:%s" % (name, distribution, version)

    _update_task(request_json['task_uuid'],
                 "creating", 
                 message_log)
    
    request_json['status'] = 1
    request_json['message_log'] = message_log

    database.update_request(request_json)
    
    logger.info(message_log)

    distribution = "%s:%s" % (distribution, version)

    dockerfile = '''
    FROM ''' + distribution + '''
    MAINTAINER Carlos Llano <carlos_llano@hotmail.com>
    RUN sed 's/#$ModLoad imudp/$ModLoad imudp/' -i /etc/rsyslog.conf
    RUN sed 's/#$UDPServerRun 514/$UDPServerRun 514/' -i /etc/rsyslog.conf
    RUN sed 's/#$ModLoad imtcp/$ModLoad imtcp/' -i /etc/rsyslog.conf
    RUN sed 's/#$InputTCPServerRun 514/$InputTCPServerRun 514/' -i /etc/rsyslog.conf
    EXPOSE 514/tcp 514/udp 
    CMD ["/usr/sbin/rsyslogd", "-dn", "-f", "/etc/rsyslog.conf"]
    RUN apt-get install -y openssh-server git
    RUN mkdir /var/run/sshd
    RUN useradd -s /bin/bash -m ''' + user + '''
    RUN echo "''' + user + ":" + password + '''" | chpasswd
    RUN echo "''' + user + ''' ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    RUN echo "root:virtshell" | chpasswd
    RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config
    RUN sed "s@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g" -i /etc/pam.d/sshd
    ENV NOTVISIBLE "in users profile"
    RUN echo "export VISIBLE=now" >> /etc/profile
    EXPOSE 22
    CMD ["/usr/sbin/sshd", "-D"]
    '''

    dockerfile_binary = BytesIO(dockerfile.encode('utf-8'))
    client = Client(version='1.20', base_url='tcp://127.0.0.1:2376')
    response = [line for line in client.build(fileobj=dockerfile_binary,
                                              rm=True,
                                              tag=distribution)]
    container = client.create_container(name=name, 
                                        image=distribution)
    container_id = container['Id']

    client.start(container_id)
    link_path = client.inspect_container(container_id)
    ip = link_path['NetworkSettings']['IPAddress']
    message_log = "docker-container-plugin %s created successfully, ipv4: %s.\n" % (name, ip)

    _update_task(request_json['task_uuid'],
                 "created",
                 message_log)

    logger.info(message_log)
    request_json['local_ipv4'] = ip
    #request_json['message_log'] += message_log  Fix this!!!

    database.update_request(request_json)

    return request_json

def _provisioning_container(request_json):
    name = request_json['name']
    ip = request_json['local_ipv4']
    builder = str(request_json['builder'])
    executor = request_json['executor']

    message_log = "docker_container_plugin provisioning docker-container %s, with ip %s..." % (name, ip)
    logger.info(message_log)
    request_json['message_log'] = message_log

    _update_task(request_json['task_uuid'],
                 "provisioning",
                 message_log)

    logger.info(request_json)

    database.update_request(request_json)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(ip, port=22, username='root', password='virtshell')
    stdin, stdout, stderr = ssh.exec_command("git clone " + builder)
    message_log = "stdout: " + str(stdout.readlines()) + " stderr: " + str(stderr.readlines())

    logger.info(message_log)

    request_json['message_log'] = message_log
    database.update_request(request_json)

    dot = builder.rfind('.')
    slash = builder.rfind('/')
    repository_name = builder[slash+1:dot]
    stdin, stdout, stderr = ssh.exec_command("cd " + repository_name + ";" + executor)
    message_log = "docker_container_plugin stdout: " + str(stdout.readlines()) + " stderr: " + str(stderr.readlines())

    logger.info(message_log)

    _update_task(request_json['task_uuid'],
                 "provisioned",
                 message_log)

    ssh.close()

    request_json['status'] = -1
    request_json['message_log'] = message_log

    database.update_request(request_json)

def start(request):
    return "successfully"

def stop(request):
    return "successfully"