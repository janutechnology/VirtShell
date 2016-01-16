import services
import json

@services.mongo
def create_host(host):
    try:
        host_id = services.mongodb.hosts.insert_one(host).inserted_id
        return {"status": "ok", "host_uuid": host['uuid']}
    except exception as e:
        return {"status": "error", "reason": e.message}

@services.mongo
def get_all_hosts():
    try:
        hosts_list = []
        hosts_json = {}
        for host in services.mongodb.hosts.find():
            del host['_id']
            hosts_list.append(host)
        return hosts_json = {"status": "ok", "hosts": hosts_list}
    except exception as e:
        return {"status": "error", "reason": e.message}

@services.mongo
def exists_host(uuid):
    try:
        host = services.mongodb.hosts.find_one({"uuid": uuid})
        if host != None:
            return {"status": "ok", "exists": True}
        else:
            return {"status": "ok", "exists": False}
    except exception as e:
        return {"status": "error", "reason": e.message}

@services.mongo
def get_host(uuid):
    try:
        host = services.mongodb.hosts.find_one({"uuid": uuid})
        if host != None:
            del host['_id']
            return {"status": "ok", "host": host}
    except exception as e:
        return {"status": "error", "reason": e.message}

@services.mongo
def delete_host(uuid):
    try:
        result = services.mongodb.hosts.delete_one({"uuid": uuid})
        return {"status": "ok"}
    except exception as e:
        return {"status": "error", "reason": e.message}