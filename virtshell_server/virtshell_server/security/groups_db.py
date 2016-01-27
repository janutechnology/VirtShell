import security
import json

@security.mongo
def create_group(group):
    try:
        group_id = security.mongodb.groups.insert_one(group).inserted_id
        return {"status": "ok", "group_uuid": group['uuid']}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def get_all_groups():
    try:
        groups_list = []
        groups_json = {}
        for group in security.mongodb.groups.find():
            del group['_id']
            groups_list.append(group)
        return {"status": "ok", "groups": groups_list}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def exists_group(uuid):
    try:
        group = security.mongodb.groups.find_one({"uuid": uuid})
        if group != None:
            return {"status": "ok", "exists": True}
        else:
            return {"status": "ok", "exists": False}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def get_group(uuid, delete_id = True):
    try:
        group = security.mongodb.groups.find_one({"uuid": uuid})
        if group != None:
            if delete_id:
                del group['_id']
            return {"status": "ok", "group": group}
        else:
            return {"status": "group not found"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def delete_group(uuid):
    try:
        result = security.mongodb.groups.delete_one({"uuid": uuid})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def update_group(uuid, updated_group):
    try:
        result = security.mongodb.groups.find_one_and_update({'uuid': uuid}, 
                                                            {'$set': updated_group})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e}