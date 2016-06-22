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

    def get_file(self, uri):
        return self.storage_db.get("uri", uri)

    def update_file(self, uri, file):
        return self.storage_db.update("uri", uri, file)

    def delete_file(self, uri):
        return self.storage_db.delete("uri", uri)