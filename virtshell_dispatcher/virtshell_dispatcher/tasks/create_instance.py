#!/usr/bin/env python

import json
import logging
import requests
import websocket
from config import VIRTSHELL_SERVER
from config import PORT_AGENT

log = None

def get_instance(instance_uuid):
    url = "%s/instances/%s" % (VIRTSHELL_SERVER, instance_uuid)
    r = requests.get(url)
    instance_data = json.loads(r.text)
    return instance_data

def get_enviroment(enviroment_name):
    url = "%s/enviroments/%s" % (VIRTSHELL_SERVER, enviroment_name)
    r = requests.get(url)
    enviroment_data = json.loads(r.text)
    return enviroment_data

def get_info_host(host_name):
    url = "%s/hosts/%s" % (VIRTSHELL_SERVER, host_name)
    r = requests.get(url)
    host_data = json.loads(r.text)
    return host_data        

def get_hosts_from_partition(partition_name):
    url = "%s/partitions/%s" % (VIRTSHELL_SERVER, partition_name)
    r = requests.get(url)
    partition_data = json.loads(r.text)
    return partition_data['hosts']

def select_host(instance_type, hosts):
    candidate_hosts = []
    if hosts is not None:
        for host_name in hosts:
            host = get_info_host(host_name)
            if instance_type == host['type']:
                if 'instances' in host:
                    number_instances = len(host['instances'])
                else:
                    number_instances = 0
                candidate_hosts.append( (host['local_ipv4'], number_instances) )

        if len(candidate_hosts)>0:
            selected_host = min(candidate_hosts, key=lambda element: element[1])
            return selected_host[0]
        else:
            raise Exception('hosts not found for instance type %s' % 
                                                       (instance_data['name']))
    else:
        raise Exception('hosts not found for partition')

def send_request_to_agent(ip_host, instance_data):
    distribution, version, arch = instance_data['operating_system'].split('-')

    data = {'action': 'create',
            'driver': instance_data['driver'],
            'name': instance_data['name'], 
            'distribution': distribution,
            'version': version,
            'arch': arch,
            'launch':1,
            'cpus':1,
            'provisioner': instance_data['provisioner'],
            'executor': instance_data['executor'],
            'user':'virtshell',
            'password':'virtshell',            
            'memory':1024}          

    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://%s:8080/" % (ip_host))
    ws.send(json.dumps(data))
    result = ws.recv()
    ws.close()
    return result

def main(task, logger):
    try:
        log = logger
        log.info("[create_instance] started...")
        instance_data = get_instance(task['object_uuid'])
        enviroment_data = get_enviroment(instance_data['enviroment'])
        hosts = get_hosts_from_partition(enviroment_data['partition'])
        ip_host_selected = select_host(instance_data['host_type'], hosts)
        response = send_request_to_agent(ip_host_selected, instance_data)
        if response == "received":
            message_response = "creating instance in host : %s" % ip_host_selected
        else:
            message_response = "error processing the task."
        return response, message_response
    except Exception as e:
        return "error", str(e)
