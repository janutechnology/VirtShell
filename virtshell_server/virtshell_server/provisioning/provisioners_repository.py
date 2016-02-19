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

    def get_provisioner(self, name):
        return self.storage_db.get("name", name)

    def update_provisioner(self, name, provisioner):
        return self.storage_db.update("name", name, provisioner)

    def delete_provisioner(self, name):
        return self.storage_db.delete("name", name)