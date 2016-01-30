import tornado.ioloop
import tornado.web
from security.users import users
import json

class UsersHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.users = users()

    def get(self, uuid=None):
        if uuid:
            result = self.users.get_user(uuid)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.users.get_all_users()
            if result['status'] == 'ok':
                users = result['documents']
                response = {'users': users}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, uuid=None):
        user = tornado.escape.json_decode(self.request.body)
        result = self.users.create_user(user)
        if result['status'] == 'ok':
            response = {"create": "success", "uuid": result['uuid']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            user = tornado.escape.json_decode(self.request.body)
            result = self.users.update_user(uuid, user)
            if result['status'] == 'ok':
                response = {"update": "success", "uuid": uuid}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

    def delete(self, uuid=None):
        if uuid:
            result = self.users.delete_user(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success", "uuid": uuid}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

UsersResources = (r'/users/(.*)', UsersHandler)