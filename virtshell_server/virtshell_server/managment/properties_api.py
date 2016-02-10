import json
import tornado.web
import tornado.ioloop
from managment.properties import Properties

class PropertiesHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.properties = Properties()

    def get(self, property_name=None, instance=None, enviroment=None):
        if property_name and instance and enviroment:
            result = self.properties.get_property(property_name, instance, enviroment)
            if result['status'] == 'ok':
                response = result['property']
            else:
                response = {'error': result['reason']}
        else:
            response = {"get": "error", "reason": "missing parameters"}
        return self.write(json.dumps(response))

PropertiesResources = (r'/properties/(.*)/instance/(.*)/enviroment/(.*)', PropertiesHandler)