import json
import tornado.web
import tornado.ioloop
from managment.partitions import Partitions

class PartitionsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.partitions = Partitions()

    def get(self, uuid=None):
        if uuid:
            result = self.partitions.get_partition(uuid)
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
            response = {"create": "success", "uuid": result['uuid']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            partition = tornado.escape.json_decode(self.request.body)
            result = self.partitions.update_partition(uuid, partition)
            if result['status'] == 'ok':
                response = {"update": "success", "uuid": uuid}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

    def delete(self, uuid=None):
        if uuid:
            result = self.partitions.delete_partition(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success", "uuid": uuid}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

PartitionsResources = (r'/partitions/(.*)', PartitionsHandler)