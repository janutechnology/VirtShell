import json
import managment
from storage import StorageFactory

class HostsRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('hosts')

    def create_host(self, host):
        return self.storage_db.create(host)

    def get_all_hosts(self):
        return self.storage_db.get()

    def get_host(self, name):
        return self.storage_db.get("name", name)

    def update_host(self, name, host):
        return self.storage_db.update("name", name, host)

    def delete_host(self, name):
        return self.storage_db.delete("name", name)       