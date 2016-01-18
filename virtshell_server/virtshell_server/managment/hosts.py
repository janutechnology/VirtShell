import managment.hosts_db
import uuid

def get_all_hosts():
    return managment.hosts_db.get_all_hosts()

def get_host(uuid):
    return managment.hosts_db.get_host(uuid)

def create_host(host):
    host['uuid'] = str(uuid.uuid4())
    return managment.hosts_db.create_host(host)

def delete_host(uuid):
    return managment.hosts_db.delete_host(uuid)