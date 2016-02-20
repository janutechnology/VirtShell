import json
import managment
from storage import StorageFactory

class InstancesRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('instances')

    def create_instance(self, instances):
        return self.storage_db.create(instances)

    def get_all_instances(self):
        return self.storage_db.get()

    def get_instance(self, name):
        return self.storage_db.get("name", name)

    def update_instance(self, name, instances):
        return self.storage_db.update("name", name, instances)

    def delete_instance(self, name):
        return self.storage_db.delete("name", name)