import security
from storage import StorageFactory
import json

class UsersRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('users')

    def create_user(self, user):
        return self.storage_db.create(user)

    def get_all_users(self):
        return self.storage_db.get()

    def get_user(self, uuid):
        return self.storage_db.get(uuid)

    def update_user(self, uuid, user):
        return self.storage_db.update(uuid, user)

    def delete_user(self, uuid):
        return self.storage_db.delete(uuid)