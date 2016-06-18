import tornado.ioloop
import tornado.web
from provisioning.images import Images
import json

class ImagesHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.images = Images()
        self.logger = logger

    def get(self, name=None):
        self.logger.info("images GET " + name)
        if name:
            result = self.images.get_image(name)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.images.get_all_images()
            if result['status'] == 'ok':
                images = result['documents']
                response = {'images': images}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, name=None):
        self.logger.info("images POST " + name)
        image = tornado.escape.json_decode(self.request.body)
        result = self.images.create_image(image)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, name=None):
        self.logger.info("images PUT " + name)
        if name:
            image = tornado.escape.json_decode(self.request.body)
            result = self.images.update_image(name, image)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

    def delete(self, name=None):
        self.logger.info("images DELETE " + name)
        if name:
            result = self.images.delete_image(name)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            response = {"delete": "error", "reason": "missing name parameter"}
        return self.write(json.dumps(response))

ImagesResources = (r'/images/(.*)', ImagesHandler)