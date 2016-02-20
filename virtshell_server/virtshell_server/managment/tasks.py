import uuid
from managment.tasks_repository import TasksRepository

class Tasks(object):
    def __init__(self):
        self.tasks_repository = TasksRepository()

    def get_all_tasks(self):
        return self.tasks_repository.get_all_tasks()

    def get_task(self, uuid):
        return self.tasks_repository.get_task(uuid)

    def get_tasks_by_status(self, status_name):
        return self.tasks_repository.get_tasks_by_status(status_name)

    def create_task(self, task):
        task['uuid'] = str(uuid.uuid4())
        result = self.tasks_repository.create_task(task)
        result['uuid'] = task['uuid']
        return result

    def update_task(self, uuid, task):
        return self.tasks_repository.update_task(uuid, task)

    def delete_task(self, name):
        return self.tasks_repository.delete_task(name)