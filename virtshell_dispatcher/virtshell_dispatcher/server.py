#!/usr/bin/env python3
 
import os
import sys
import imp
import time
import json
import urllib
import logger
import os.path
import logging
import requests
import logging.handlers
from config import VIRTSHELL_SERVER

class Dispatcher(object):
    def __init__(self):
        self.logger = logger.get_logger('virtshell_dispatcher')
        self.listeners_tasks = {}
        self.tasks_folder = "./tasks"
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

    def execute_task(self, task):
        if task['type'] in self.listeners_tasks:
            module, function = self.listeners_tasks[task['type']]
            self.update_task(task['uuid'], 'dispatching', 'creating message to agent')
            status, message = function(task, self.logger)
            if status != "error":
                self.logger.info(message)
            else:
                self.logger.error(message)
            self.update_task(task['uuid'], status, message)
        else:
            self.logger.info("task not supported...")
            self.update_task(task['uuid'], 'error', 'task not supported')

    def run(self):
        while True:
            pending_tasks = self.get_pending_tasks()
            for task in pending_tasks:
                self.execute_task(task)
            time.sleep(20)

    def get_pending_tasks(self):
        self.logger.info("Get pending tasks from server...")
        url = "%s/tasks/status/pending" % (VIRTSHELL_SERVER)
        try:
            data = requests.get(url)             
            pending_tasks = json.loads(data.text)['tasks']
            self.logger.info("Number of tasks pending: " + str(len(pending_tasks)))
            return pending_tasks
        except requests.exceptions.RequestException as e:
            self.logger.error("The server does not respond...")
            return []

    def update_task(self, task_uuid, state , log):
        url = "%s/tasks/%s" % (VIRTSHELL_SERVER, task_uuid)
        r = requests.put(url, data = json.dumps({'status': state, 'log': log}))

if __name__ == "__main__":
    dispatcher = Dispatcher()
    dispatcher.run()
