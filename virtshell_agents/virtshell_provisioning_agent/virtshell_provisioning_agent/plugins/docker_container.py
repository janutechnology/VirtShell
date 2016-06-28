import os
import io
import sys
import json
import time
import zlib
import config
import base64
import logging
import paramiko
import requests
import linecache
import subprocess
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
    r = requests.get(url)
    return( str( base64.b64decode(r.text.encode('utf-8')), 'utf-8' ) )

def _get_current_home_path():
    home = os.curdir
    if 'HOME' in os.environ:
        home = os.environ['HOME']
    elif os.name == 'posix':
        home = os.path.expanduser("~/")
    elif os.name == 'nt':
        if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
            home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
    else:
        home = os.environ['HOMEPATH']
    return home

def _create_container(request_json):
    name = request_json['name']
    distribution = request_json['distribution']
    version = request_json['version']
    user = request_json['user']
    password = request_json['password']

    message_log = "downloading dockerfile from %s" % request_json['image']

    _update_task(request_json['task_uuid'],
                 "setting up", 
                 message_log)
    
    request_json['status'] = 1
    request_json['message_log'] = message_log

    database.update_request(request_json)
    
    logger.info(message_log)

    image_tag = "vs_%s:%s" % (distribution, version)

    dockerfile_content = _get_dockerfile(request_json['image'])

    directory_dockerfile_path = os.path.join(config.PATH_STATIC_DOCKERFILES, distribution + "_" + version)
    if not os.path.exists(directory_dockerfile_path):
        os.makedirs(directory_dockerfile_path)

    dockerfile_path = os.path.join(directory_dockerfile_path, "Dockerfile")
    file_handler = open(dockerfile_path, 'w')
    file_handler.write(dockerfile_content)
    file_handler.close()

    message_log = "docker_container_plugin creating docker-container %s... with %s:%s" % (name, distribution, version)

    _update_task(request_json['task_uuid'],
                 "creating", 
                 message_log)
    
    request_json['status'] = 1
    request_json['message_log'] = message_log

    database.update_request(request_json)
    
    logger.info(message_log)    

    image_name = "vs/%s:%s" % (distribution, version)
    command = ['docker','build','-t', image_name, directory_dockerfile_path]
    response = execute_command(command)

    command = ['docker', 'run', '-d', '-P', '--name', name, image_name]
    response = execute_command(command)

    command = ['docker', 'inspect', '--format', '''{{ .Id }}''', name]
    container_id = execute_command(command)

    command = ['docker', 'inspect', '--format', '''{{ .NetworkSettings.IPAddress }}''', container_id.strip()]
    ip = execute_command(command)
    ip = ip.strip()

    current_home_path = _get_current_home_path()
    current_home_ssh_known_hosts = os.path.join(current_home_path, ".ssh/known_hosts")

    command = ['ssh-keygen', '-f', current_home_ssh_known_hosts , '-R', ip]
    response = execute_command(command)

    message_log = "docker-container-plugin %s created successfully, ipv4: %s.\n" % (name, ip)

    _update_task(request_json['task_uuid'],
                 "created",
                 message_log)

    logger.info(message_log)
    request_json['local_ipv4'] = str(ip.strip())
    #request_json['message_log'] += message_log  Fix this!!!

    database.update_request(request_json)

    return request_json

def _provisioning_container(request_json):
    try:
        name = request_json['name']
        ip = request_json['local_ipv4']
        builder = str(request_json['builder'])
        executor = request_json['executor']

        message_log = "docker_container_plugin provisioning docker-container %s, with ip %s" % (name, ip)
        logger.info(message_log)
        request_json['message_log'] = message_log

        _update_task(request_json['task_uuid'],
                     "provisioning",
                     message_log)

        logger.info(request_json)

        database.update_request(request_json)

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()
            ssh.connect(ip, 
                        port=22, 
                        username='root', 
                        password='virtshell')
        except Exception as e:
            print ('*** Failed to connect reason:',e )

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

def execute_command(command):
    lines=""
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        lines = lines + line
    return lines

def start(request):
    return "successfully"

def stop(request):
    return "successfully"