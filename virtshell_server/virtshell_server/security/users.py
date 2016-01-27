import security.users_db
import uuid

def get_all_users():
    return security.users_db.get_all_users()

def get_user(uuid):
    return security.users_db.get_user(uuid)

def create_user(user):
    user['uuid'] = str(uuid.uuid4())
    return security.users_db.create_user(user)

def delete_user(uuid):
    return security.users_db.delete_user(uuid)

def update_user(uuid, user):
    return security.users_db.update_user(uuid, user)