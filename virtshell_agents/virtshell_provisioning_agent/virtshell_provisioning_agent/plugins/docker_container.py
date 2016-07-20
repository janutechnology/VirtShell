import os
import io
import sys
import json
import time
import zlib
import config
import base64
import logging
import requests
import linecache
import subprocess
import urllib.request
from io import BytesIO
from docker import Client
from subprocess import call
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
        time.sleep(5)
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
    image = request_json['image']

    message_log = "downloading dockerfile from %s" % request_json['image']

    _update_task(request_json['task_uuid'],
                 "setting up", 
                 message_log)
    
    request_json['status'] = 1
    request_json['message_log'] = message_log

    database.update_request(request_json)
    
    logger.info(message_log)

    directory_dockerfile_path = _create_dockerfile(image, distribution, version)

    message_log = "docker_container_plugin creating docker-container %s... with %s:%s" % (name, distribution, version)

    _update_task(request_json['task_uuid'],
                 "creating", 
                 message_log)
    
    request_json['status'] = 1
    request_json['message_log'] = message_log

    database.update_request(request_json)
    
    logger.info(message_log)

    image_name = _build_container(distribution, version, directory_dockerfile_path)
    response = _start_container(name, image_name)
    ip = _get_ip_container(name)

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

        message_log = _clone_repository(config.SSH_USER, ip, builder)

        logger.info(message_log)
        request_json['message_log'] = message_log
        database.update_request(request_json)

        dot = builder.rfind('.')
        slash = builder.rfind('/')
        repository_name = builder[slash+1:dot]

        message_log = _execute_provisioner(config.SSH_USER, ip, repository_name, executor)

        logger.info(message_log)

        _update_task(request_json['task_uuid'],
                     "provisioned",
                     message_log)

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

def _create_dockerfile(image, distribution, version):
    dockerfile_content = _get_dockerfile(image)

    directory_dockerfile_path = os.path.join(config.PATH_STATIC_DOCKERFILES, distribution + "_" + version)
    if not os.path.exists(directory_dockerfile_path):
        os.makedirs(directory_dockerfile_path)

    # Get the ssh key of host and put into the dockerfile 
    ssh_rsa_pub_content = _get_ssh_key_rsa_pub()

    dockerfile_path = os.path.join(directory_dockerfile_path, "Dockerfile")
    file_handler = open(dockerfile_path, 'w')
    file_handler.write(dockerfile_content)

    # Add the ssh pub key of the host server into the docker file
    file_handler.write("\n\n")
    file_handler.write("RUN mkdir /root/.ssh\n")
    file_handler.write("RUN touch " + config.AUTHORIZED_KEYS_LOCATION + "\n")
    file_handler.write("RUN echo '" + ssh_rsa_pub_content + "' >> " + config.AUTHORIZED_KEYS_LOCATION + "\n")
    file_handler.close()

    return directory_dockerfile_path

def _build_container(distribution, version, directory_dockerfile_path):
    image_name = "vs/%s:%s" % (distribution, version)
    command = ['docker','build','-t', image_name, directory_dockerfile_path]
    response = _execute_command(command)
    return image_name

def _start_container(name, image_name):
    command = ['docker', 'run', '-d', '-P', '--name', name, image_name]
    return _execute_command(command)

def _get_ip_container(name):
    command = ['docker', 'inspect', '--format', '''{{ .Id }}''', name]
    container_id = _execute_command(command)

    command = ['docker', 'inspect', '--format', '''{{ .NetworkSettings.IPAddress }}''', container_id.strip()]
    ip = _execute_command(command)
    ip = ip.strip()

    command = ['sudo', 'ssh-keygen', '-f', config.SSH_KNOWN_HOSTS , '-R', ip]
    response = _execute_command(command)
    return ip

def _get_ssh_key_rsa_pub():
    return _execute_command(['sudo', 'cat', config.RSA_PUB_KEY_LOCATION])

def _clone_repository(user, ip, builder):
    return _execute_command(['sudo', 'ssh', '-o', 'StrictHostKeyChecking=no', user+'@'+ip, 'git', 'clone', builder])

def _execute_provisioner(user, ip, repository_name, executor):
    return _execute_command(['sudo', 'ssh', '-o', 'StrictHostKeyChecking=no', user+'@'+ip, "cd " + repository_name + ";" + executor])

def _execute_command(command):
    lines=""
    output = subprocess.check_output(command)
    return output.decode("utf-8").strip()

def start(request):
    return "successfully"

def stop(request):
    return "successfully"