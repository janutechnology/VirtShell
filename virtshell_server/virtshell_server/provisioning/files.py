from provisioning.files_repository import FilesRepository
import uuid
import config
import os
import json

class Files(object):
    def __init__(self):
        self.files_repository = FilesRepository()
        self.static_path = config.PATH_STATIC_FILES

    def get_all_files(self):
        return self.files_repository.get_all_files()

    def get_file(self, uri):
        return self.files_repository.get_file(uri)

    def create_file(self, file_content, file_name, directory_path, permissions):
        directory = os.path.join(self.static_path, directory_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)

        file_handler = open(file_path, 'w')
        file_handler.write(file_content.decode('utf-8'))
        file_handler.close()

        file_data = {}
        file_data['uuid'] = str(uuid.uuid4())
        file_data['name'] = file_name
        file_data['directory_path'] = directory_path
        file_data['location'] = file_path
        file_data['permissions'] = permissions
        file_data['uri'] = config.URL_STATIC_FILES + directory_path + "/" + file_name

        result = self.files_repository.create_file(file_data)
        if result['status'] == 'ok':
            result['uri'] = file_data['uri']
        return result

    def delete_file(self, uri):
        file_json = self.get_file(uri)

        if file_json['status'] == 'ok':
            file_path = file_json['document']['location']

            if os.path.isfile(file_path):
                os.remove(file_path)
                path, filename = os.path.split(file_path)

                try:
                    # remove the paht if the directory is empty
                    os.rmdir(path)
                except OSError:
                    pass
                return self.files_repository.delete_file(uri)
            else:
                result = {}
                result['status'] = 'error'
                result['reason'] = 'file not exists in location ' + file_path
                return result
        else:
            return file_json

    def update_file(self, uri, file_content, permissions):
        file_json = self.get_file(uri)

        if file_json['status'] == 'ok':
            if file_content != None:
                file_path = file_json['document']['location']

                if os.path.isfile(file_path):
                    file_handler = open(file_path, 'w')
                    file_handler.write(file_content.decode('utf-8'))
                    file_handler.close()
                else:
                    result['status'] = 'error'
                    result['reason'] = 'file not exists in location ' + file_path

            result = {}
            if permissions != None:
                file_data = {}
                file_data['permissions'] = permissions
                return self.files_repository.update_file(uri, file_data)
            else:
                result['status'] = 'ok'
            return result
        else:
            return file_json