import tornado.ioloop
import tornado.web
import provisioning.provisioners
import json

class ProvisionersHandler(tornado.web.RequestHandler):
    def get(self, uuid=None):
        if uuid:
            return self.write(json.dumps(provisioning.provisioners.get_provisioner(uuid)))
        return self.write(json.dumps(provisioning.provisioners.get_all_provisioners()))

    def post(self, uuid=None):
        provisioner = tornado.escape.json_decode(self.request.body)
        return self.write(provisioning.provisioners.create_provisioner(provisioner))

    def put(self, uuid=None):
        if uuid:
            provisioner = tornado.escape.json_decode(self.request.body)
            return self.write(provisioning.provisioners.update_provisioner(uuid, provisioner))

    def delete(self, uuid=None):
        if uuid:
            return self.write(provisioning.provisioners.delete_provisioner(uuid))

ProvisionersResources = (r'/provisioners/(.*)', ProvisionersHandler)