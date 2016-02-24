#!/usr/bin/env python
 
import sys
import time
import json
import logging
import requests
import websocket
from daemon import Daemon
from config import VIRTSHELL_SERVER
import logging.handlers
 
class Dispatcher(Daemon):
    def __init__(self, pid_file):
        Daemon.__init__(self, pid_file)
        self.init_logger("virtshell_dispatcher")

    def run(self):
        while True:
            pending_tasks = self.get_pending_tasks()
            for task in pending_tasks:
                if task['type'] == 'create_instance':                        
                    instance_data = self.get_instance(task['object_uuid'])
                    ip_host = self.select_host(task, instance_data)
                    if ip_host:
                        self.send_request_to_agent(ip_host, instance_data)                        
                else:
                    self.logger.info("task not supported...")
                    self.update_task(task, 'failed', 'task not supported')
            time.sleep(10)

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

    def get_instance(self, instance_uuid):
        url = "%s/instances/%s" % (VIRTSHELL_SERVER, instance_uuid)
        r = requests.get(url)
        instance_data = json.loads(r.text)
        return instance_data

    def select_host(self, task, instance_data):
        enviroment_name = instance_data['enviroment']
        url = "%s/enviroments/%s" % (VIRTSHELL_SERVER, enviroment_name)
        try:
            r = requests.get(url)
            enviroment = json.loads(r.text)
            partition_name = enviroment['partition']
            hosts = self.get_hosts_from_partition(partition_name)
            if hosts is not None:
                for host_name in hosts:
                    host = self.get_info_host(host_name)
                    if instance_data['type'] == host['type']:
                        return host['local_ipv4']
                self.logger.error("host not found for instance %s" % 
                                                        (instance_data['name']))
                self.update_task(task, 
                                 'failed', 
                                 'host type not found for instance')
            else:
                self.logger.error("host not found for instance %s" % 
                                                        (instance_data['name']))
                self.update_task(task, 
                                 'failed', 
                                 'There is not hosts in partition %s' % 
                                                               (partition_name))
        except:
            self.logger.error("The server does not respond...")
        return None

    def update_task(self, task, state , log):
        url = "%s/tasks/%s" % (VIRTSHELL_SERVER, task['uuid'])
        r = requests.put(url, data = {'status': state, 'log': log})

    def get_info_host(self, host_name):
        url = "%s/hosts/%s" % (VIRTSHELL_SERVER, host_name)
        r = requests.get(url)
        host_data = json.loads(r.text)
        return host_data        

    def get_hosts_from_partition(self, partition_name):
        url = "%s/partitions/%s" % (VIRTSHELL_SERVER, partition_name)
        try:
            r = requests.get(url)
            partition_data = json.loads(r.text)
            return partition_data['hosts']
        except:
            self.logger.error("The server does not respond...")
            return None      

    def send_request_to_agent(self, ip_host, instance_data):
        websocket.enableTrace(True)
        ws = websocket.create_connection("ws://%s:8080/" % (ip_host))
        ws.send(json.dumps(data))
        self.logger.info("dispatching request to create new instance...")
        result = ws.recv()
        # Validar la respuesta, y actualizar el estado de la tarea
        self.logger.info("receiving response from agent: ", result)
        ws.close()        

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

