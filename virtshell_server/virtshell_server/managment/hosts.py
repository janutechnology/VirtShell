import managment.hosts_db
import uuid

class Hosts(object):
    def __init__(self):
        host_repository = managment.hosts_repository.HostsRepository()

    def get_all_hosts():
        return hosts_repository.get_all_hosts()

    def get_host(uuid):
        return hosts_repository.get_host(uuid)

    def create_host(host):
        host['uuid'] = str(uuid.uuid4())
        return hosts_repository.create_host(host)

    def delete_host(uuid):
        return hosts_repository.delete_host(uuid)

    def update_host(uuid, host):
        return hosts_repository.update_host(uuid, host)