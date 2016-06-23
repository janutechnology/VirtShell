from provisioning.files_repository import FilesRepository
import uuid
import config
import os
import json

class Files(object):
    def __init__(self):
        self.files_repository = FilesRepository()
        self.static_path = config.PATH_STATIC_FILES
        self.url_static_path = config.URL_STATIC_FILES

    def get_all_files(self):
        return self.files_repository.get_all_files()

    def get_file(self, name):
        return self.files_repository.get_file(name)

    def get_content(self, file_name):
        result = {}
        try:
            file_json = self.get_file(file_name)
            file_path = file_json['document']['location']
            with open(file_path, 'r') as content_file:
                content = content_file.read()
            result['status'] = 'ok'
            result['content_file'] = content
            return result
        except Exception as e:
            result['status'] = 'error'
            result['reason'] = e

    def create_file(self, file_content, file_name, permissions):        
        if not os.path.exists(self.static_path):
            os.makedirs(directory)

        file_path = os.path.join(self.static_path, file_name)
        if os.path.isfile(file_path):
            result = {}
            result['status'] = 'error'
            result['reason'] = 'file already exists'
            return result

        file_handler = open(file_path, 'w')
        file_handler.write(file_content.decode('utf-8'))
        file_handler.close()

        file_data = {}
        file_data['uuid'] = str(uuid.uuid4())
        file_data['name'] = file_name
        file_data['location'] = file_path
        file_data['permissions'] = permissions
        file_data['uri'] = os.path.join(self.url_static_path, file_name)

        result = self.files_repository.create_file(file_data)
        if result['status'] == 'ok':
            result['uri'] = file_data['uri']
        return result

    def delete_file(self, name):
        file_json = self.get_file(name)

        if file_json['status'] == 'ok':
            file_path = file_json['document']['location']

            if os.path.isfile(file_path):
                os.remove(file_path)
                path, filename = os.path.split(file_path)
                return self.files_repository.delete_file(name)
            else:
                result = {}
                result['status'] = 'error'
                result['reason'] = 'file not exists in location ' + file_path
                return result
        else:
            return file_json

    def update_file(self, file_name, file_content, permissions):
        file_json = self.get_file(file_name)

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
                return self.files_repository.update_file(file_name, file_data)
            else:
                result['status'] = 'ok'
            return result
        else:
            return file_json