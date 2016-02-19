import tornado.ioloop
import tornado.web
from security.users import Users
import json

class UsersHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.users = Users()

    def get(self, name=None):
        if name:
            result = self.users.get_user(name)
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

    def post(self, name=None):
        user = tornado.escape.json_decode(self.request.body)
        result = self.users.create_user(user)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        if name:
            user = tornado.escape.json_decode(self.request.body)
            result = self.users.update_user(name, user)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        if name:
            result = self.users.delete_user(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

UsersResources = (r'/users/(.*)', UsersHandler)