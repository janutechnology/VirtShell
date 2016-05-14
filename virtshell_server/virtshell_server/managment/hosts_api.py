import json
import tornado.web
import tornado.ioloop
import logger
from managment.hosts import Hosts

class HostsHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.hosts = Hosts()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("hosts GET " + name)
        if name:
            result = self.hosts.get_host(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.hosts.get_all_hosts()
            if result['status'] == 'ok':
                hosts = result['documents']
                response = {'hosts': hosts}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        self.logger.info("hosts POST " + name)
        host = tornado.escape.json_decode(self.request.body)
        result = self.hosts.create_host(host)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        self.logger.info("hosts PUT " + name)
        if name:
            host = tornado.escape.json_decode(self.request.body)
            result = self.hosts.update_host(name, host)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        self.logger.info("hosts DELETE " + name)
        if name:
            result = self.hosts.delete_host(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

HostsResources = (r'/hosts/(.*)', HostsHandler)