import json
import tornado.web
import tornado.ioloop
from managment.instances import Instances

class InstancesHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.instances = Instances()

    def get(self, name=None):
        if name:
            result = self.instances.get_instance(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.instances.get_all_instances()
            if result['status'] == 'ok':
                instances = result['documents']
                response = {'instances': instances}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        instance = tornado.escape.json_decode(self.request.body)
        result = self.instances.create_instance(instance)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error"}
        return self.write(json.dumps(response))

    def put(self, name=None):
        if name:
            instance = tornado.escape.json_decode(self.request.body)
            result = self.instances.update_instance(name, instance)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        if name:
            result = self.instances.delete_instance(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

InstancesResources = (r'/instances/(.*)', InstancesHandler)