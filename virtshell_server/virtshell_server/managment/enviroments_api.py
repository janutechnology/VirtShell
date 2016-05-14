import json
import tornado.web
import tornado.ioloop
from managment.enviroments import Enviroments

class EnviromentsHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.enviroments = Enviroments()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("enviroments GET " + name)
        if name:
            result = self.enviroments.get_enviroment(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.enviroments.get_all_enviroments()
            if result['status'] == 'ok':
                enviroments = result['documents']
                response = {'enviroments': enviroments}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        self.logger.info("enviroments POST " + name)
        enviroment = tornado.escape.json_decode(self.request.body)
        result = self.enviroments.create_enviroment(enviroment)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        self.logger.info("enviroments DELETE " + name)
        if name:
            result = self.enviroments.delete_enviroment(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

EnviromentsResources = (r'/enviroments/(.*)', EnviromentsHandler)