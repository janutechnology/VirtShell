import json
import managment
from storage import StorageFactory

class EnviromentsRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('enviroments')

    def create_enviroment(self, enviroment):
        return self.storage_db.create(enviroment)

    def get_all_enviroments(self):
        return self.storage_db.get()

    def get_enviroment(self, name):
        return self.storage_db.get("name", name)

    def delete_enviroment(self, name):
        return self.storage_db.delete("name", name)       