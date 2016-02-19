import tornado.ioloop
import tornado.web
from provisioning.provisioners import Provisioners
import json

class ProvisionersHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.provisioners = Provisioners()

    def get(self, name=None):
        if name:
            result = self.provisioners.get_provisioner(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.provisioners.get_all_provisioners()
            if result['status'] == 'ok':
                provisioners = result['documents']
                response = {'provisioners': provisioners}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        provisioner = tornado.escape.json_decode(self.request.body)
        result = self.provisioners.create_provisioner(provisioner)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        if name:
            provisioner = tornado.escape.json_decode(self.request.body)
            result = self.provisioners.update_provisioner(name, provisioner)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        if name:
            result = self.provisioners.delete_provisioner(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

ProvisionersResources = (r'/provisioners/(.*)', ProvisionersHandler)