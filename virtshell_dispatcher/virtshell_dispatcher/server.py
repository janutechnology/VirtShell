#!/usr/bin/env python3
 
import os
import sys
import imp
import time
import json
import urllib
import os.path
import logging
import requests
import logging.handlers
from daemon import Daemon
from config import VIRTSHELL_SERVER
import logging.handlers
 
class Dispatcher(object):
    def __init__(self):
        self.init_logger("virtshell_dispatcher")
        self.listeners_tasks = {}
        self.tasks_folder = "/home/callanor/virtshell_dispatcher/virtshell_dispatcher/tasks"
        self.special_files = ["__init__.py", "__pycache__"]
        self.task_execute_method = "main"       
        self.load_plugin_tasks()
        self.logger.info("service started...")

    def load_plugin_tasks(self):
        self.logger.info("finding plugins tasks...")
        number_plugin_tasks = 0
        possible_plugins_tasks = os.listdir(self.tasks_folder)
        possible_plugins_tasks = [task for task in possible_plugins_tasks if task not in self.special_files]
        for module in possible_plugins_tasks:
            if not module.endswith(".pyc") and not os.path.isdir(module):
                module = os.path.splitext(module)[0]
                info = imp.find_module(module, [self.tasks_folder])
                plugin_task_class = imp.load_module(module, *info)
                execute_method = getattr(plugin_task_class, 
                                         self.task_execute_method)
                self.listeners_tasks[module] = (plugin_task_class, 
                                                execute_method)
                self.logger.info("task %s.py found" % module)
        self.logger.info("plugins tasks finished...")

    def execute_task(self, task_name, task):
        if task_name in self.listeners_tasks:
            module, function = self.listeners_tasks[task_name]
            status, message = function(task)
            if status != "error":
                self.logger.info(message)
            else:
                self.logger.error(message)
            self.update_task(task, status, message)
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
        self.logger.info(url)
        try:
            data = requests.get(url)             
            pending_tasks = json.loads(data.text)['tasks']
            self.logger.info("Number of tasks pending: " + str(len(pending_tasks)))
            return pending_tasks
        except requests.exceptions.RequestException as e:
            self.logger.error("The server does not respond...", e)
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
    dispatcher = Dispatcher()
    dispatcher.run()