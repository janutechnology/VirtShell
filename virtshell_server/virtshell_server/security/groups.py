from security.groups_repository import GroupsRepository
import uuid

class Groups(object):
    def __init__(self):
        self.groups_repository = GroupsRepository()

    def get_all_groups(self):
        return self.groups_repository.get_all_groups()

    def get_group(self, name):
        return self.groups_repository.get_group(name)

    def create_group(self, group):
        group['uuid'] = str(uuid.uuid4())
        return self.groups_repository.create_group(group)

    def delete_group(self, name):
        return self.groups_repository.delete_group(name)

    def update_group(self, name, group):
        return self.groups_repository.update_group(name, group)