#!/usr/bin/env python

import json
import logging
import requests
import websocket
from config import VIRTSHELL_SERVER
from config import PORT_AGENT
from config import USER
from config import PASSWORD

log = None

def get_instance(instance_uuid):
    url = "%s/instances/%s" % (VIRTSHELL_SERVER, instance_uuid)
    r = requests.get(url)
    instance_data = json.loads(r.text)
    return instance_data

def get_image(image_name):
    url = "%s/images/%s" % (VIRTSHELL_SERVER, image_name)
    r = requests.get(url)
    image_data = json.loads(r.text)
    return image_data

def get_enviroment(enviroment_name):
    url = "%s/enviroments/%s" % (VIRTSHELL_SERVER, enviroment_name)
    r = requests.get(url)
    enviroment_data = json.loads(r.text)
    return enviroment_data

def get_provisioner(provisioner_name):
    url = "%s/provisioners/%s" % (VIRTSHELL_SERVER, provisioner_name)
    r = requests.get(url)
    provisioner_data = json.loads(r.text)
    return provisioner_data


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

def select_host(instance_type, driver, hosts):
    candidate_hosts = []
    if hosts is not None:
        for host_name in hosts:
            host = get_info_host(host_name)
            if instance_type == host['type'] and driver in host['drivers']:
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

def send_request_to_agent(ip_host, instance_data, image_data, provisioner_data, task):
    # For example: ubuntu_server_14.04.2_amd64
    operating_system, type_operating_system, version, architecture = provisioner_data['image'].split('_')

    launch = instance_data['launch'] if 'launch' in instance_data else 1

    data = {'task_uuid': task['uuid'],
            'instance_uuid': task['object_uuid'],
            'action': 'create',
            'driver': instance_data['driver'],
            'name': instance_data['name'], 
            'distribution': operating_system,
            'version': version,
            'arch': architecture,
            'launch': launch,
            'cpus': instance_data['cpus'],
            'builder': provisioner_data['builder'],
            'executor': provisioner_data['executor'],
            'image' : image_data['container_resource'] if 'container_resource' in image_data else "",
            'user': USER,
            'password': PASSWORD,
            'memory': instance_data['memory']}

    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://%s:8080/" % (ip_host))
    ws.send(json.dumps(data))
    result = ws.recv()
    ws.close()
    return result

def main(task, logger):
    try:
        log = logger
        log.info("[dispatch create_instance] started...")
        instance_data = get_instance(task['object_uuid'])
        enviroment_data = get_enviroment(instance_data['enviroment'])
        hosts = get_hosts_from_partition(enviroment_data['partition'])
        ip_host_selected = select_host(instance_data['host_type'],
                                       instance_data['driver'],
                                       hosts)
        log.info("[dispatcher ip_host_selected]: " + ip_host_selected)
        provisioner_data = get_provisioner(instance_data['provisioner'])
        image_data = get_image(provisioner_data['image'])
        response = send_request_to_agent(ip_host_selected, 
                                         instance_data,
                                         image_data,
                                         provisioner_data,
                                         task)
        if response == "received":
            message_response = "task dispatched to host: %s" % ip_host_selected
            status = "dispatched"
        else:
            message_response = "error dispatching the task."
            status = "error"
        return status, message_response
    except Exception as e:
        return "error", "Exception: " + str(e)
