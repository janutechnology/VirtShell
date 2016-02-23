#!/usr/bin/env python
 
import sys
import time
import json
import logging
import requests
from daemon import Daemon
from config import VIRTSHELL_SERVER
import logging.handlers
 
class Dispatcher(Daemon):
    def __init__(self, pid_file):
        Daemon.__init__(self, pid_file)
        self.init_logger("virtshell_dispatcher")

    def run(self):
        while True:
            self.logger.info("Get pending tasks from server...")
            url = "%s/tasks/status/pending" % (VIRTSHELL_SERVER)
            try:
                r = requests.get(url)
                pending_tasks = json.loads(r.text)
                for task in pending_tasks['tasks']:
                    if task['type'] == 'create_instance':
                        instance_uuid = task['object_uuid']
                        url = "%s/instances/%s" % (VIRTSHELL_SERVER,
                                                   instance_uuid)
                        r = requests.get(url)
                        instance_data = json.loads(r.text)
                        self.logger.info(instance_data)
            except:
                self.logger.error("The server does not respond...")
            time.sleep(10)

    def init_logger(self, LoggerName):
        # Create logger
        self.logger = logging.getLogger(LoggerName)
        self.logger.setLevel(logging.INFO)
        # Create handler

        handler = logging.FileHandler('/var/log/virtshell_dispatcher.log')
        #handler = SysLogHandler(address='/dev/log')
        handler.setLevel(logging.INFO)
        # Create formatter
        formatter = logging.Formatter('%(asctime)s %(name)s '
                                      '%(levelname)s %(message)s')
        # Add formatter and handler
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
 
if __name__ == "__main__":
    dispatcher = Dispatcher('/var/run/virtshell_dispatcher/dispatcher.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            dispatcher.start()
        elif 'stop' == sys.argv[1]:
            dispatcher.stop()
        elif 'restart' == sys.argv[1]:
            dispatcher.restart()
        else:
            print ("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print ("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)

