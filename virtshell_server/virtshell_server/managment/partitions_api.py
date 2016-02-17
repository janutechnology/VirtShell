import json
import tornado.web
import tornado.ioloop
from managment.partitions import Partitions

class PartitionsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.partitions = Partitions()

    def get(self, name=None):
        if name:
            result = self.partitions.get_partition(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.partitions.get_all_partitions()
            if result['status'] == 'ok':
                partitions = result['documents']
                response = {'partitions': partitions}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, uuid=None):
        partition = tornado.escape.json_decode(self.request.body)
        result = self.partitions.create_partition(partition)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        if name:
            partition = tornado.escape.json_decode(self.request.body)
            result = self.partitions.update_partition(name, partition)
            if result['status'] == 'ok':
                response = {"update": "success", "name": name}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        if name:
            result = self.partitions.delete_partition(name)
            if result['status'] == 'ok':
                response = {"delete": "success", "name": name}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

PartitionsResources = (r'/partitions/(.*)', PartitionsHandler)