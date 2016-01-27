import tornado.ioloop
import tornado.web
import security.groups
import json

class GroupsHandler(tornado.web.RequestHandler):
    def get(self, uuid=None):
        if uuid:
            return self.write(json.dumps(security.groups.get_group(uuid)))
        return self.write(json.dumps(security.groups.get_all_groups()))

    def post(self, uuid=None):
        group = tornado.escape.json_decode(self.request.body)
        return self.write(security.groups.create_group(group))

    def put(self, uuid=None):
        if uuid:
            group = tornado.escape.json_decode(self.request.body)
            return self.write(security.groups.update_group(uuid, group))

    def delete(self, uuid=None):
        if uuid:
            return self.write(security.groups.delete_group(uuid))

GroupsResources = (r'/groups/(.*)', GroupsHandler)