import provisioning
from storage import StorageFactory
import json

class ImagesRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('images')

    def create_image(self, image):
        return self.storage_db.create(image)

    def get_all_images(self):
        return self.storage_db.get()

    def get_image(self, name):
        return self.storage_db.get("name", name)

    def update_image(self, name, image):
        return self.storage_db.update("name", name, image)

    def delete_image(self, name):
        return self.storage_db.delete("name", name)