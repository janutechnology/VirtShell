import security
import json

@security.mongo
def create_user(user):
    try:
        user_id = security.mongodb.users.insert_one(user).inserted_id
        return {"status": "ok", "user_uuid": user['uuid']}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def get_all_users():
    try:
        users_list = []
        users_json = {}
        for user in security.mongodb.users.find():
            del user['_id']
            users_list.append(user)
        return {"status": "ok", "users": users_list}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def exists_user(uuid):
    try:
        user = security.mongodb.users.find_one({"uuid": uuid})
        if user != None:
            return {"status": "ok", "exists": True}
        else:
            return {"status": "ok", "exists": False}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def get_user(uuid, delete_id = True):
    try:
        user = security.mongodb.users.find_one({"uuid": uuid})
        if user != None:
            if delete_id:
                del user['_id']
            return {"status": "ok", "user": user}
        else:
            return {"status": "user not found"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def delete_user(uuid):
    try:
        result = security.mongodb.users.delete_one({"uuid": uuid})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e.message}

@security.mongo
def update_user(uuid, updated_user):
    try:
        result = security.mongodb.users.find_one_and_update({'uuid': uuid}, 
                                                            {'$set': updated_user})
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "reason": e}