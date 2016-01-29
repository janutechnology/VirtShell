import managment
import storage
import json

class HostsRepository(object):
    def __init__(self):
        storage_db = storage.MongoDB('hosts')

    def create_host(self, host):
        return storage_db.create(host)

    def get_all_hosts(self):
        return storage_db.get()

    def get_host(self, uuid):
        return storage_db.get(uuid)

    def update_host(self, uuid, host):
        return storage_db.update(uuid, host)

    def delete_host(self, uuid):
        return storage_db.delete()