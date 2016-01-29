import tornado.ioloop
import tornado.web
from managment.hosts import Hosts
import json

class HostsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.hosts = Hosts()

    def get(self, uuid=None):
        if uuid:
            result = self.hosts.get_host(uuid)
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

    def post(self, uuid=None):
        host = tornado.escape.json_decode(self.request.body)
        result = self.hosts.create_host(host)
        if result['status'] == 'ok':
            response = {"create": "success", "uuid": result['uuid']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            host = tornado.escape.json_decode(self.request.body)
            result = self.hosts.update_host(uuid, host)
            if result['status'] == 'ok':
                response = {"update": "success", "uuid": uuid}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

    def delete(self, uuid=None):
        if uuid:
            result = self.hosts.delete_host(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success", "uuid": uuid}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

HostsResources = (r'/hosts/(.*)', HostsHandler)