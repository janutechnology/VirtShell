import managment
import json

@managment.mongo
def create_host(host):
    try:
        host_id = managment.mongodb.hosts.insert_one(host).inserted_id
        return {"status": "ok", "host_uuid": host['uuid']}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@managment.mongo
def get_all_hosts():
    try:
        hosts_list = []
        hosts_json = {}
        for host in managment.mongodb.hosts.find():
            del host['_id']
            hosts_list.append(host)
        return {"status": "ok", "hosts": hosts_list}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@managment.mongo
def exists_host(uuid):
    try:
        host = managment.mongodb.hosts.find_one({"uuid": uuid})
        if host != None:
            return {"status": "ok", "exists": True}
        else:
            return {"status": "ok", "exists": False}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@managment.mongo
def get_host(uuid, delete_id = True):
    try:
        host = managment.mongodb.hosts.find_one({"uuid": uuid})
        if host != None:
            if delete_id:
                del host['_id']
            return {"status": "ok", "host": host}
        else:
            return {"status": "host not found"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@managment.mongo
def delete_host(uuid):
    try:
        result = managment.mongodb.hosts.delete_one({"uuid": uuid})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@managment.mongo
def update_host(uuid, updated_host):
    try:
        result = managment.mongodb.hosts.find_one_and_update({'uuid': uuid}, 
                                                             {'$set': updated_host})         
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e}