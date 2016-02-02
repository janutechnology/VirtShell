from managment.properties_repository import PropertiesRepository

class Properties(object):
    def __init__(self):
        self.properties_repository = PropertiesRepository()

    def get_property(self, property_name, instance, enviroment):
        return self.properties_repository.get_property(property_name,
                                                       instance, 
                                                       enviroment)