import tornado.ioloop
import tornado.web
import security.users
import json

class UsersHandler(tornado.web.RequestHandler):
    def get(self, uuid=None):
        if uuid:
            return self.write(json.dumps(security.users.get_user(uuid)))
        return self.write(json.dumps(security.users.get_all_users()))

    def post(self, uuid=None):
        user = tornado.escape.json_decode(self.request.body)
        return self.write(security.users.create_user(user))

    def put(self, uuid=None):
        if uuid:
            user = tornado.escape.json_decode(self.request.body)
            return self.write(security.users.update_user(uuid, user))

    def delete(self, uuid=None):
        if uuid:
            return self.write(security.users.delete_user(uuid))

UsersResources = (r'/users/(.*)', UsersHandler)