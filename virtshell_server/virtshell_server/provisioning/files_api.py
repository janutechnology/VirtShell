import tornado.ioloop
import tornado.web
from provisioning.files import Files
import json

class FilesHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.files = Files()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("files GET " + name)
        if name:
            result = self.files.get_file(name)
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
        file = tornado.escape.json_decode(self.request.body)
        result = self.files.create_file(file)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        self.logger.info("files PUT " + name)
        if name:
            file = tornado.escape.json_decode(self.request.body)
            result = self.files.update_file(name, file)
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