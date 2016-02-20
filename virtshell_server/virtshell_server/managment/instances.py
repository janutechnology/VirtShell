import uuid
from managment.instances_repository import InstancesRepository

class Instances(object):
    def __init__(self):
        self.instances_repository = InstancesRepository()

    def get_all_instances(self):
        return self.instances_repository.get_all_instances()

    def get_instance(self, name):
        return self.instances_repository.get_instance(name)

    def create_instance(self, instance):
        instance['uuid'] = str(uuid.uuid4())
        return self.instances_repository.create_instance(instance)

    def delete_instance(self, name):
        return self.instances_repository.delete_instance(name)

    def update_instance(self, name, instance):
        return self.instances_repository.update_instance(name, instance)