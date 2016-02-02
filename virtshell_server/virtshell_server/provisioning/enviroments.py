from provisioning.enviroments_repository import EnviromentsRepository
import uuid

class Enviroments(object):
    def __init__(self):
        self.enviroments_repository = EnviromentsRepository()

    def get_all_enviroments(self):
        return self.enviroments_repository.get_all_enviroments()

    def get_enviroment(self, name):
        return self.enviroments_repository.get_enviroment(name)

    def create_enviroment(self, enviroment):
        enviroment['uuid'] = str(uuid.uuid4())
        return self.enviroments_repository.create_enviroment(enviroment)

    def delete_enviroment(self, name):
        return self.enviroments_repository.delete_enviroment(name)