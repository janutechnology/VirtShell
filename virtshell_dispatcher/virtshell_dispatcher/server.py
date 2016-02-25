#!/usr/bin/env python
 
import os
import sys
import time
import json
import os.path
import logging
import requests
from daemon import Daemon
from config import VIRTSHELL_SERVER
import logging.handlers
 
class Dispatcher(Daemon):
    def __init__(self, pid_file):
        Daemon.__init__(self, pid_file)
        self.listeners_tasks = {}
        self.tasks_folder = "./tasks"
        self.special_files = ["__init__.py", "__pycache__"]
        self.task_execute_method = "main"
        self.load_plugin_tasks()
        self.init_logger("virtshell_dispatcher started...")

    def load_plugin_tasks(self):
        self.logger.info("finding plugins tasks...")
        possible_plugins_tasks = os.listdir(self.tasks_folder)
        possible_plugins_tasks = [task for task in possible_plugins_tasks if task not in special_files]
        for module in possible_plugins_tasks:
            if not module.endswith(".pyc") and not os.path.isdir(module):
                module = os.path.splitext(module)[0]
                info = imp.find_module(module, [self.tasks_folder])
                plugin_task_class = imp.load_module(module, *info)
                execute_method = getattr(plugin_task_class, 
                                         self.task_execute_method)
                self.listeners_tasks[module] = (plugin_task_class, 
                                                self.execute_method)
                self.logger.info("task %s.py found" % module)

    def execute_task(self, task_name, task):
        if task_name in self.listeners_tasks:
            module, function = self.listeners_tasks[task_name]
            return function(task, self.logger)
        else:
            self.logger.info("task not supported...")
            self.update_task(task, 'failed', 'task not supported')

    def run(self):
        while True:
            pending_tasks = self.get_pending_tasks()
            for task in pending_tasks:
                self.execute_task(task['type'], task)
            time.sleep(20)

    def get_pending_tasks(self):
        self.logger.info("Get pending tasks from server...")
        url = "%s/tasks/status/pending" % (VIRTSHELL_SERVER)
        try:
            r = requests.get(url)
            pending_tasks = json.loads(r.text)
            self.logger.info("Number of tasks pending: ", len(pending_tasks))
            return pending_tasks['tasks']
        except:
            self.logger.error("The server does not respond...")
            return []

    def update_task(self, task, state , log):
        url = "%s/tasks/%s" % (VIRTSHELL_SERVER, task['uuid'])
        r = requests.put(url, data = {'status': state, 'log': log})    

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

