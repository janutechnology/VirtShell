import uuid
from managment.partitions_repository import PartitionsRepository

class Partitions(object):
    def __init__(self):
        self.partitions_repository = PartitionsRepository()

    def get_all_partitions(self):
        return self.partitions_repository.get_all_partitions()

    def get_partition(self, name):
        return self.partitions_repository.get_partition(name)

    def create_partition(self, partition):
        partition['uuid'] = str(uuid.uuid4())
        return self.partitions_repository.create_partition(partition)

    def delete_partition(self, name):
        return self.partitions_repository.delete_partition(name)

    def update_partition(self, name, partition):
        return self.partitions_repository.update_partition(name, partition)

    def add_host(self, name, host):
        return self.partitions_repository.add_host(name, host)        