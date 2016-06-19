from provisioning.files_repository import FilesRepository
import uuid

class Files(object):
    def __init__(self):
        self.files_repository = FilesRepository()

    def get_all_files(self):
        return self.files_repository.get_all_files()

    def get_file(self, name):
        return self.files_repository.get_file(name)

    def create_file(self, file):
        file['uuid'] = str(uuid.uuid4())
        return self.files_repository.create_file(file)

    def delete_file(self, name):
        return self.files_repository.delete_file(name)

    def update_file(self, name, file):
        return self.files_repository.update_file(name, file)