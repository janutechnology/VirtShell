import services
import json

@services.mongo
def create_host(host):
    host_id = services.mongodb.hosts.insert_one(host).inserted_id
    return {"create": "success", "uuid": host['uuid']}

@services.mongo
def get_all_hosts():
    hosts_list = []
    hosts_json = {}
    for host in services.mongodb.hosts.find():
        del host['_id']
        hosts_list.append(host)
    hosts_json = {"hosts" : hosts_list}
    return hosts_json

