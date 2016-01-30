from provisioning.provisioners_repository import ProvisionersRepository
import uuid

class Provisioners(object):
    def __init__(self):
        self.provisioners_repository = ProvisionersRepository()

    def get_all_provisioners(self):
        return self.provisioners_repository.get_all_provisioners()

    def get_provisioner(self, uuid):
        return self.provisioners_repository.get_provisioner(uuid)

    def create_provisioner(self, provisioner):
        provisioner['uuid'] = str(uuid.uuid4())
        return self.provisioners_repository.create_provisioner(provisioner)

    def delete_provisioner(self, uuid):
        return self.provisioners_repository.delete_provisioner(uuid)

    def update_provisioner(self, uuid, provisioner):
        return self.provisioners_repository.update_provisioner(uuid, provisioner)