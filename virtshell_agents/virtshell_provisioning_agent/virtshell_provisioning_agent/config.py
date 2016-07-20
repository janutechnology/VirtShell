"""
VirtShell-Provisioning-Agent High Level Server Configurations
"""
LOGGER = "syslog"  #file
LOG_FILE = "/var/janu/log/virtshell_provisioning_agent.log"
VIRTSHELL_SERVER = "http://192.168.56.103:80"
ISO_DIR = "/var/janu/isos"
PATH_STATIC_DOCKERFILES = "/var/janu/dockerfiles/"
AUTHORIZED_KEYS_LOCATION = "/root/.ssh/authorized_keys"
RSA_PUB_KEY_LOCATION = '/root/.ssh/id_rsa.pub'
SSH_KNOWN_HOSTS = '/root/.ssh/known_hosts'
SSH_USER = 'root'