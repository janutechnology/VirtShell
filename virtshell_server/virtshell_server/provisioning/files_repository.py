import provisioning
from storage import StorageFactory
import json

class FilesRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('files')

    def create_file(self, file):
        return self.storage_db.create(file)

    def get_all_files(self):
        return self.storage_db.get()

    def get_file(self, name):
        return self.storage_db.get("name", name)

    def update_file(self, name, file):
        return self.storage_db.update("name", name, file)

    def delete_file(self, name):
        return self.storage_db.delete("name", name)