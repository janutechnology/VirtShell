import tornado.ioloop
import tornado.web
from security.groups import Groups
import json

class GroupsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.groups = Groups()

    def get(self, uuid=None):
        if uuid:
            result = self.groups.get_group(uuid)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.groups.get_all_groups()
            if result['status'] == 'ok':
                groups = result['documents']
                response = {'groups': groups}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, uuid=None):
        group = tornado.escape.json_decode(self.request.body)
        result = self.groups.create_group(group)
        if result['status'] == 'ok':
            response = {"create": "success", "uuid": result['uuid']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            group = tornado.escape.json_decode(self.request.body)
            result = self.groups.update_group(uuid, group)
            if result['status'] == 'ok':
                response = {"update": "success", "uuid": uuid}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

    def delete(self, uuid=None):
        if uuid:
            result = self.groups.delete_group(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success", "uuid": uuid}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

GroupsResources = (r'/groups/(.*)', GroupsHandler)