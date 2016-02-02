import managment
from storage import StorageFactory
import json

class PropertiesRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('instances')

    def get_property(self, property_name, instance, enviroment):
        return self.storage_db.get_property(property_name, instance, enviroment)