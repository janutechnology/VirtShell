import managment
import storage.mongodb
from storage.mongodb import MongoDB
import json

class HostsRepository(object):
    def __init__(self):
        print("HostsRepository...")
        self.storage_db = MongoDB('hosts')
        print ("HostsRepository finished....")

    def create_host(self, host):
        return self.storage_db.create(host)

    def get_all_hosts(self):
        return self.storage_db.get()

    def get_host(self, uuid):
        return self.storage_db.get(uuid)

    def update_host(self, uuid, host):
        print("..........3................")
        return self.storage_db.update(uuid, host)

    def delete_host(self, uuid):
        return self.storage_db.delete()