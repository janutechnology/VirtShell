import json
import managment
from storage import StorageFactory

class PartitionsRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('partitions')

    def create_partition(self, host):
        return self.storage_db.create(host)

    def get_all_partitions(self):
        return self.storage_db.get()

    def get_partition(self, uuid):
        return self.storage_db.get(uuid)

    def update_partition(self, uuid, host):
        return self.storage_db.update(uuid, host)

    def delete_partition(self, uuid):
        return self.storage_db.delete(uuid)