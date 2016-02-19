import tornado.ioloop
import tornado.web
from security.groups import Groups
import json

class GroupsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.groups = Groups()

    def get(self, name=None):
        if name:
            result = self.groups.get_group(name)
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

    def post(self, name=None):
        group = tornado.escape.json_decode(self.request.body)
        result = self.groups.create_group(group)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        if name:
            group = tornado.escape.json_decode(self.request.body)
            result = self.groups.update_group(name, group)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        if name:
            result = self.groups.delete_group(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

GroupsResources = (r'/groups/(.*)', GroupsHandler)