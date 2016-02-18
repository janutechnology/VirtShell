import uuid
from managment.partitions import Partitions
from managment.hosts_repository import HostsRepository

class Hosts(object):
    def __init__(self):
        self.hosts_repository = HostsRepository()

    def get_all_hosts(self):
        return self.hosts_repository.get_all_hosts()

    def get_host(self, name):
        return self.hosts_repository.get_host(name)

    def create_host(self, host):
        partitions = Partitions()
        result = partitions.add_host(host['partition'], host['name'])
        if result['status'] == 'ok':
            host['uuid'] = str(uuid.uuid4())
            return self.hosts_repository.create_host(host)
        else:
            return {"add_host": "error", "reason": result['reason']}

    def delete_host(self, name):
        return self.hosts_repository.delete_host(name)

    def update_host(self, name, host):
        return self.hosts_repository.update_host(name, host)