import uuid
from managment.partitions_repository import PartitionsRepository

class Partitions(object):
    def __init__(self):
        self.partitions_repository = PartitionsRepository()

    def get_all_partitions(self):
        return self.partitions_repository.get_all_partitions()

    def get_partition(self, uuid):
        return self.Partitions_repository.get_partition(uuid)

    def create_partition(self, partition):
        partition['uuid'] = str(uuid.uuid4())
        return self.partitions_repository.create_partition(partition)

    def delete_partition(self, uuid):
        return self.partitions_repository.delete_partition(uuid)

    def update_partition(self, uuid, partition):
        return self.partitions_repository.update_partition(uuid, partition)