import security
from storage import StorageFactory
import json

class GroupsRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('groups')

    def create_group(self, group):
        return self.storage_db.create(group)

    def get_all_groups(self):
        return self.storage_db.get()

    def get_group(self, uuid):
        return self.storage_db.get(uuid)

    def update_group(self, uuid, group):
        return self.storage_db.update(uuid, group)

    def delete_group(self, uuid):
        return self.storage_db.delete(uuid)