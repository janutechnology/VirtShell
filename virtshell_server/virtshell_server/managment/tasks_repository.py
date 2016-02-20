import json
import managment
from storage import StorageFactory

class TasksRepository(object):
    def __init__(self):
        self.storage_db = StorageFactory.get_storage('tasks')

    def get_all_tasks(self):
        return self.storage_db.get()

    def get_task(self, uuid):
        return self.storage_db.get(uuid)

    def get_tasks_by_status(self, status_name):
        return self.storage_db.get_all_tasks_by_status(status_name)

    def create_task(self, task):
        return self.storage_db.create(task)

    def update_task(self, uuid, task):
        return self.storage_db.update("uuid", uuid, task)

    def delete_task(self, uuid):
        return self.storage_db.delete("uuid", uuid)