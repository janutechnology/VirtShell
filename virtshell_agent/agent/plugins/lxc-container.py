import json
import time
import subprocess
from exceptions import PluginException

class Container(object):
    def __init__(self, logger):
        self.logger = logger

    def create(self, request):        
        try:
            name = request.message['name']
            distribution = request.message['distribution']
            release = request.message['release']
            arch = request.message['arch']
            user = request.message['user']
            password = request.message['password']
            self.logger.info("[lxc_container] creating container %s", name)
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
                             arch]])
            self.logger.info("[lxc_container] container %s created successfully." % 
                             name)
            request.message_log += "container created successfully\n"
            request = self.start(request)
            request = self._install_openssh_server(request)
            request = self._create_user(request)
        except Exception as err:
            message_error = "[lxc_container] Error: Failed to create the \
                             container, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

    def start(self, request):
        try:
            name = request.message['name']
            self.logger.info("[lxc_container] starting container %s", name)
            subprocess.call(["lxc-start", "-n", name])
            self.logger.info("[lxc_container] container %s started \
                              successfully." % name)
            request.message_log += "container started successfully\n"
            time.sleep(10)
        except Exception as err:
            message_error = "[lxc_container] Error: Failed to start \
                             the container, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

    def stop(self, request):
        try:
            name = request.message['name']
            self.logger.info("[lxc_container] stoping container %s", name)
            subprocess.call(["lxc-stop", "-n", name])
            self.logger.info("[lxc_container] container %s stoped \
                              successfully." % name)
            request.message_log += "container stoped successfully\n"
            time.sleep(10)
        except Exception as err:
            message_error = "[lxc_container] Error: Failed to stop the \
                             container, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

    def _install_openssh_server(self, request):
        try:
            name = request.message['name']
            self.logger.info("[lxc_container] installing openssh-server \
                              in container %s" % name)
            subprocess.call(["lxc-attach", 
                             "-n", 
                             name,
                             "--",
                             "apt-get",
                             "install",
                             "-y",
                             "openssh-server"])
            self.logger.info("[lxc_container] openssh-server installed \
                              successfully in container %s" % name)
            request.message_log += "openssh-server installed successfully\n"
        except Exception as err:
            message_error = "[lxc_container] Error: Failed to install \
                             openssh-server in container, %s" % err
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

    def _create_user(self, request):
        try:
            name = request.message['name']
            user = request.message['user']
            password = request.message['password']
            self.logger.info("[lxc_container] creating user in \
                              container %s" % name)
            path = "/var/lib/lxc/%s/rootfs/" % name
            subprocess.call(["chroot",
                             path,
                        name, user, password     "useradd",
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
            self.logger.info("[lxc_container] user %s created successfully \
                              in container %s" % (user,name))
            request.message_log += "user %s created successfully\n" % user
        except Exception as err:
            message_error = "[lxc_container] Error: Failed to create the \
                              user %s in container %s, %s" % (user, name, err)
            self.logger.error(message_error)
            raise PluginException(message_error)
        return request

def run(logger, request):
    container = Container(logger)
    action = request.message['action']
    if action == 'create':
        return container.create(request)
    elif action == 'start':
        return container.start(request)