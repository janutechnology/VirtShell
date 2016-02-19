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

    def get_user(self, name):
        return self.storage_db.get("username", name)

    def update_user(self, name, user):
        return self.storage_db.update("username", name, user)

    def delete_user(self, name):
        return self.storage_db.delete("username", name)