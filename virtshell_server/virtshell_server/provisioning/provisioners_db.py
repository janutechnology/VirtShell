import provisioning
import json

@provisioning.mongo
def create_provisioner(provisioner):
    try:
        provisioner_id = provisioning.mongodb.provisioners.insert_one(provisioner).inserted_id
        return {"status": "ok", "provisioner_uuid": provisioner['uuid']}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@provisioning.mongo
def get_all_provisioners():
    try:
        provisioners_list = []
        provisioners_json = {}
        for provisioner in provisioning.mongodb.provisioners.find():
            del provisioner['_id']
            provisioners_list.append(provisioner)
        return {"status": "ok", "provisioners": provisioners_list}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@provisioning.mongo
def exists_provisioner(uuid):
    try:
        provisioner = provisioning.mongodb.provisioners.find_one({"uuid": uuid})
        if provisioner != None:
            return {"status": "ok", "exists": True}
        else:
            return {"status": "ok", "exists": False}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@provisioning.mongo
def get_provisioner(uuid, delete_id = True):
    try:
        provisioner = provisioning.mongodb.provisioners.find_one({"uuid": uuid})
        if provisioner != None:
            if delete_id:
                del provisioner['_id']
            return {"status": "ok", "provisioner": provisioner}
        else:
            return {"status": "provisioner not found"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@provisioning.mongo
def delete_provisioner(uuid):
    try:
        result = provisioning.mongodb.provisioners.delete_one({"uuid": uuid})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@provisioning.mongo
def update_provisioner(uuid, updated_provisioner):
    try:
        result = provisioning.mongodb.provisioners.find_one_and_update({'uuid': uuid}, 
                                                            {'$set': updated_provisioner})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e}