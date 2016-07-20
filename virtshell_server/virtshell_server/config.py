"""
VirtShell-Server High Level Server Configurations
"""
DATABASE_PROVIDER = "mongodb"
MONGODB = "mongodb://localhost:27017"
DATABASE_NAME = "virtshell_server_db"
PORT = 80
LOGGER = "syslog"  #file
LOG_FILE = "/var/janu/log/virtshell_server.log"
URL_STATIC_FILES = "http://192.168.56.103/file/"
PATH_STATIC_FILES = "/var/janu/files/"
