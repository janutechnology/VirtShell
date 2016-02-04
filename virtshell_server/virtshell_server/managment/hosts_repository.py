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

    def get_host(self, uuid):
        return self.storage_db.get(uuid)

    def update_host(self, uuid, host):
        return self.storage_db.update(uuid, host)

    def delete_host(self, uuid):
        return self.storage_db.delete(uuid)