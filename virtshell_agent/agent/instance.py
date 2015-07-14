class Instance(object):
    def __init__(self):
        self._price = None

    def create_instance(self):
        return self._price

class InstanceFactory(object):
    @staticmethod
    def create_instance(instance_type):
        if instance_type == 'vmachine':
            return VirtualMachine()
        elif instance_type == 'container':
            return Container()