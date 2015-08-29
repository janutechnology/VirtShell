import lxc
import sys

def create_container(logger, request):
    container = lxc.Container(request.message['name'])
    if container.defined:
        logger.error("[lxc_container] Error: container already exists ")
        return -1

    logger.info("[lxc_container] creating container %s", request.message['name'])
    if not container.create("download", 
                            lxc.LXC_CREATE_QUIET, 
                            {"dist": request.message['distribution'],
                             "release": request.message['release'],
                             "arch": request.message['arch']}):
        logger.error("[lxc_container] Error: Failed to create the container\
                     rootfs", file=sys.stderr)
        return -1
    logger.info("[lxc_container] container %s created successfully." % 
                                                        request.message['name'])

    if not container.start():
        logger.error("[lxc_container] Error: Failed to start the container")
        return -1

    # ----------------------------------------------------------------------
    # Pending to Send to server the container state and container pid
    # ----------------------------------------------------------------------
    logger.info("[lxc_container] container %s state: %s" % 
                                                    (request.message['name'],
                                                     container.state))
    logger.info("[lxc_container] container %s pid: %s" % 
                                                    (request.message['name'],
                                                     container.init_pid))

    logger.info("[lxc_container] creating user in container %s" % 
                                                    request.message['name'])
    container.attach_wait(lxc.attach_run_command,
                          ["useradd", 
                           "--create-home", 
                           "-s", 
                           "/bin/bash", 
                           request.message['user']])
    logger.info("[lxc_container] user %s created successfully in container %s" % 
                                                    (request.message['user'],
                                                     request.message['name']))
    logger.info("[lxc_container] installing packages in container %s" %
                                                    request.message['name'])
    container.attach_wait(lxc.attach_run_command,
                          ["apt-get", "install", "-y", "openssh-client"])
    container.attach_wait(lxc.attach_run_command,
                          ["apt-get", "install", "-y", "openssh-server"])
    container.attach_wait(lxc.attach_run_command,
                          ["update-rc.d", "ssh", "defaults"])
    logger.info("[lxc_container] packages installed successfully in container %s" %
                                                    request.message['name'])

    return 1

#https://www.stgraber.org/2014/02/05/lxc-1-0-scripting-with-the-api/
def run(logger, request):
    if request.message['action'] == 'create':
        return create_container(logger, request)