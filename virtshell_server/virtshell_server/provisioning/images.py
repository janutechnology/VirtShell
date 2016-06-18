from provisioning.images_repository import ImagesRepository
import uuid

class Images(object):
    def __init__(self):
        self.images_repository = ImagesRepository()

    def get_all_images(self):
        return self.images_repository.get_all_images()

    def get_image(self, name):
        return self.images_repository.get_image(name)

    def create_image(self, image):
        image['uuid'] = str(uuid.uuid4())
        return self.images_repository.create_image(image)

    def delete_image(self, name):
        return self.images_repository.delete_image(name)

    def update_image(self, name, image):
        return self.images_repository.update_image(name, image)