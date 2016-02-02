import instances
from storage import StorageFactory
import json

class InstancesRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('instances')

    def create_instance(self, instances):
        return self.storage_db.create(instances)

    def get_all_instances(self):
        return self.storage_db.get()

    def get_instance(self, uuid):
        return self.storage_db.get(uuid)

    def update_instance(self, uuid, instances):
        return self.storage_db.update(uuid, instances)

    def delete_instance(self, uuid):
        return self.storage_db.delete(uuid)