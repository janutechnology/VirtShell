from container import Container
from machine import Machine

class InstanceFactory():
    @staticmethod
    def create_instance(instance_type):
        if instance_type == 'vmachine':
            return Machine()
        elif instance_type == 'container':
            return Container()