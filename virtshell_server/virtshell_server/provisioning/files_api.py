import tornado.ioloop
import tornado.web
from provisioning.files import Files
import json
import os

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

        directory_path = self.get_argument("directory_path",
                                           default=None,
                                           strip=False)

        if directory_path != None:
            permissions = self.get_argument("permissions",
                                            default=None,
                                            strip=False)

            result = self.files.create_file(file_content,
                                            file_name,
                                            directory_path,
                                            permissions)
            if result['status'] == 'ok':
                response = {"create": "success", "uri": result['uri']}
            else:
                response = {"create": "error", "reason": result['reason']}
            return self.write(json.dumps(response))
        else:
            response = {"create": "error", "reason": "missing directory_path"}
            return self.write(json.dumps(response))

    def put(self, uri=None):
        self.logger.info("files PUT " + uri)
        try:
            file_content = self.request.files['file'][0]['body']
        except KeyError:
            file_content = None
        permissions = self.get_argument("permissions", default=None, strip=False)
        if uri:
            result = self.files.update_file(uri, file_content, permissions)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uri parameter"}
        return self.write(json.dumps(response))

    def delete(self, uri=None):
        self.logger.info("files DELETE " + uri)
        if uri:
            result = self.files.delete_file(uri)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uri parameter"}
        return self.write(json.dumps(response))

FilesResources = (r'/files/(.*)', FilesHandler)