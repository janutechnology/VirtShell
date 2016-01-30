import provisioning
from storage import StorageFactory
import json

class ProvisionersRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('provisioners')

    def create_provisioner(self, provisioner):
        return self.storage_db.create(provisioner)

    def get_all_provisioners(self):
        return self.storage_db.get()

    def get_provisioner(self, uuid):
        return self.storage_db.get(uuid)

    def update_provisioner(self, uuid, provisioner):
        return self.storage_db.update(uuid, provisioner)

    def delete_provisioner(self, uuid):
        return self.storage_db.delete(uuid)