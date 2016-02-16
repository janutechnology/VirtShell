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

    def get_partition(self, name):
        return self.storage_db.get("name", name)

    def update_partition(self, name, host):
        return self.storage_db.update("name", name, host)

    def delete_partition(self, name):
        return self.storage_db.delete("name", name)