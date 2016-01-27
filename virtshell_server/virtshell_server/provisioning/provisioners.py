import provisioning.provisioners_db
import uuid

def get_all_provisioners():
    return provisioning.provisioners_db.get_all_provisioners()

def get_provisioner(uuid):
    return provisioning.provisioners_db.get_provisioner(uuid)

def create_provisioner(provisioner):
    provisioner['uuid'] = str(uuid.uuid4())
    return provisioning.provisioners_db.create_provisioner(provisioner)

def delete_provisioner(uuid):
    return provisioning.provisioners_db.delete_provisioner(uuid)

def update_provisioner(uuid, provisioner):
    return provisioning.provisioners_db.update_provisioner(uuid, provisioner)