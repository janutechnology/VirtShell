import json
import tornado.web
import tornado.ioloop
from managment.instances import Instances

class InstancesHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.instances = Instances()

    def get(self, uuid=None):
        if uuid:
            result = self.instances.get_instance(uuid)
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

    def post(self, uuid=None):
        instance = tornado.escape.json_decode(self.request.body)
        result = self.instances.create_instance(instance)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            instance = tornado.escape.json_decode(self.request.body)
            result = self.instances.update_instance(uuid, instance)
            if result['status'] == 'ok':
                response = {"update": "success", "uuid": uuid}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

    def delete(self, uuid=None):
        if uuid:
            result = self.instances.delete_instance(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success", "uuid": uuid}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

InstancesResources = (r'/instances/(.*)', InstancesHandler)