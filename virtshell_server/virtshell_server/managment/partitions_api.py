import json
import tornado.web
import tornado.ioloop
import config as CONFIG
from managment.partitions import Partitions

class PartitionsHostHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.partitions = Partitions()
        self.logger = logger

    def put(self, name=None, host=False):
        self.logger.info("partitions PUT name: " + name + "host: " + host)
        if name and host:
            result = self.partitions.add_host(name, host)
            if result['status'] == 'ok':
                response = {"add_host": "success"}
            else:
                response = {"add_host": "error", "reason": result['reason']}
        elif not name and not host_name:
            response = {"update": "error", "reason": "missing name and host parameters"}
        return self.write(json.dumps(response))

class PartitionsHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.partitions = Partitions()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("partitions GET " + name)
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

    def post(self, name=None):
        self.logger.info("partitions POST")
        partition = tornado.escape.json_decode(self.request.body)
        result = self.partitions.create_partition(partition)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        self.logger.info("partitions PUT " + name)
        if name:
            partition = tornado.escape.json_decode(self.request.body)
            result = self.partitions.update_partition(name, partition)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        self.logger.info("partitions DELETE " + name)
        if name:
            result = self.partitions.delete_partition(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))


PartitionsHostResources = (r'/partition/(.+)/host/(.+)', PartitionsHostHandler)
PartitionsResources = (r'/partitions/(.*)', PartitionsHandler)
