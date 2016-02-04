import uuid
from managment.hosts_repository import HostsRepository

class Hosts(object):
    def __init__(self):
        self.hosts_repository = HostsRepository()

    def get_all_hosts(self):
        return self.hosts_repository.get_all_hosts()

    def get_host(self, uuid):
        return self.hosts_repository.get_host(uuid)

    def create_host(self, host):
        host['uuid'] = str(uuid.uuid4())
        return self.hosts_repository.create_host(host)

    def delete_host(self, uuid):
        return self.hosts_repository.delete_host(uuid)

    def update_host(self, uuid, host):
        return self.hosts_repository.update_host(uuid, host)