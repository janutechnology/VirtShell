import uuid
from managment.tasks import Tasks
from managment.instances_repository import InstancesRepository

class Instances(object):
    def __init__(self):
        self.instances_repository = InstancesRepository()

    def get_all_instances(self):
        return self.instances_repository.get_all_instances()

    def get_instance(self, name):
        return self.instances_repository.get_instance(name)

    def create_instance(self, instance):
        task_uuid = self._create_task("Create a new instance %s using driver %s" 
                                        % (instance['name'],instance['driver']))
        instance['uuid'] = str(uuid.uuid4())
        instance['task_uuid'] = task_uuid
        return self.instances_repository.create_instance(instance)

    def delete_instance(self, name):
        return self.instances_repository.delete_instance(name)

    def update_instance(self, name, instance):
        return self.instances_repository.update_instance(name, instance)

    def _create_task(self, description):
        task = {}
        task['description'] = description
        task['status'] = "pending"
        task['type'] = "create_instance"
        tasks = Tasks()
        result = tasks.create_task(task)
        if result['status'] == 'ok':
            return result['uuid']
        else:
            return result
        return task