import sys
import json
import time
import config
import logging
import paramiko
import requests
import linecache
import urllib.request
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

def _get_dockerfile(url):
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    return r.content

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

    #distribution = "%s:%s" % (distribution, version)

    dockerfile = _get_dockerfile(request_json['image'])

    dockerfile_binary = BytesIO(dockerfile)
    client = Client(version='1.20', base_url='tcp://127.0.0.1:2376')
    response = [line for line in client.build(fileobj=dockerfile_binary,
                                              rm=True,
                                              tag=request_json['image'])]
    container = client.create_container(name=name, 
                                        image=request_json['image'])
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
    try:
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
    except:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        reason = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
        message_error = "Failed to create the container %s, reason: %s" % (request_json['name'], reason)
        logger.error(message_error)
        request_json['status'] = 2
        request_json['message_log'] = message_error
        database.update_request(request_json)
        raise

def start(request):
    return "successfully"

def stop(request):
    return "successfully"