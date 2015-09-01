import subprocess
import json
import time

def create_container(logger, request):
    try:
        logger.info("[lxc_container] creating container %s", request.message['name'])
        subprocess.call(["lxc-create", 
                         "-t", 
                         "download", 
                         "-n", 
                         request.message['name'],
                         "--",
                         "--dist",
                         request.message['distribution'],
                         "--release",
                         request.message['release'],
                         "--arch",
                         request.message['arch']])
        logger.info("[lxc_container] container %s created successfully." % 
                                                        request.message['name'])
    except Exception as err:
        logger.error("[lxc_container] Error: Failed to create the container, %s" % err)
        return -1

    path = "/var/lib/lxc/%s/rootfs/" % request.message['name']

    try:
        logger.info("[lxc_container] starting container %s", request.message['name'])
        subprocess.call(["lxc-start", 
                         "-n", 
                         request.message['name']])
        logger.info("[lxc_container] container %s started successfully." % 
                                                        request.message['name'])
    except Exception as err:
        logger.error("[lxc_container] Error: Failed to start the container, %s" % err)
        return -1

    time.sleep(10)

    try:
        logger.info("[lxc_container] installing openssh-server in container %s" % 
                                                        request.message['name'])
        subprocess.call(["lxc-attach", 
                         "-n", 
                         request.message['name'],
                         "--",
                         "apt-get",
                         "install",
                         "-y",
                         "openssh-server"])
        logger.info("[lxc_container] openssh-server installed successfully in container %s" % 
                                                        request.message['name'])
    except Exception as err:
        logger.error("[lxc_container] Error: Failed to install openssh-server in container, %s" % err)
        return -1   

    try:
        logger.info("[lxc_container] creating user in container %s" % 
                                                        request.message['name'])
        subprocess.call(["chroot",
                         path,
                         "useradd",
                         "--create-home", 
                         "-s", 
                         "/bin/bash",
                         request.message['user']])
        user_password = "\"" + request.message['user'] + ":" + request.message['password'] + "\""
        cmd = "echo \"%s:%s\" | sudo chroot %s chpasswd" % (request.message['user'],
                                                            request.message['password'],
                                                            path)
        subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
        logger.info("[lxc_container] user %s created successfully in container %s" % 
                                                        (request.message['user'],
                                                         request.message['name']))
    except Exception as err:
        logger.error("[lxc_container] Error: Failed to create\
         the user %s in container, %s" % (request.message['user'],
                                          request.message['name']))
        return -1
    logger.info("[lxc_container] container %s created successfully." % 
                                                    (request.message['name']))
    return 1

def run(logger, request):
    if request.message['action'] == 'create':
        return create_container(logger, request)