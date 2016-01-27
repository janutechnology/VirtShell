import tornado.ioloop
import tornado.web
import managment.hosts
import json

class HostsHandler(tornado.web.RequestHandler):
    def get(self, uuid=None):
        if uuid:
            return self.write(json.dumps(managment.hosts.get_host(uuid)))
        return self.write(json.dumps(managment.hosts.get_all_hosts()))

    def post(self, uuid=None):
        host = tornado.escape.json_decode(self.request.body)
        return self.write(managment.hosts.create_host(host))

    def put(self, uuid=None):
        if uuid:
            host = tornado.escape.json_decode(self.request.body)
            return self.write(managment.hosts.update_host(uuid, host))

    def delete(self, uuid=None):
        if uuid:
            return self.write(managment.hosts.delete_host(uuid))

HostsResources = (r'/hosts/(.*)', HostsHandler)