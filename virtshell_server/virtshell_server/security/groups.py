import security.groups_db
import uuid

def get_all_groups():
    return security.groups_db.get_all_groups()

def get_group(uuid):
    return security.groups_db.get_group(uuid)

def create_group(group):
    group['uuid'] = str(uuid.uuid4())
    return security.groups_db.create_group(group)

def delete_group(uuid):
    return security.groups_db.delete_group(uuid)

def update_group(uuid, group):
    return security.groups_db.update_group(uuid, group)