import tornado.ioloop
import tornado.web
from provisioning.files import Files
import json
import os

class FileHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.files = Files()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("file GET name: " + name)
        if name:
            result = self.files.get_content(name)
            if result['status'] == 'ok':
                response = result['content_file']
            else:
                response = {'error': result['reason']}
        else:
            response = {"get": "error", "reason": "missing name"}
        return self.write(json.dumps(response))

class FilesHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.files = Files()
        self.logger = logger

    def get(self, uri=None):
        self.logger.info("files GET " + uri)
        if uri:
            result = self.files.get_file(uri)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.files.get_all_files()
            if result['status'] == 'ok':
                files = result['documents']
                response = {'files': files}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        self.logger.info("files POST " + name)
        try:
            file_content = self.request.files['file'][0]['body']
            file_name = self.request.files['file'][0]['filename']
        except KeyError:
            response = {"create": "error", "reason": "missing file"}
            return self.write(json.dumps(response))

        permissions = self.get_argument("permissions",
                                        default="xwrxwrxwr",
                                        strip=False)

        result = self.files.create_file(file_content,
                                        file_name,
                                        permissions)
        if result['status'] == 'ok':
            response = {"create": "success", "uri": result['uri']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))


    def put(self, name=None):
        self.logger.info("files PUT " + name)
        try:
            file_content = self.request.files['file'][0]['body']
        except KeyError:
            file_content = None
        permissions = self.get_argument("permissions", 
                                        default=None, 
                                        strip=False)
        if name:
            result = self.files.update_file(name, file_content, permissions)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        self.logger.info("files DELETE " + name)
        if name:
            result = self.files.delete_file(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

FilesResources = (r'/files/(.*)', FilesHandler)
FileResource = (r'/file/(.*)', FileHandler)