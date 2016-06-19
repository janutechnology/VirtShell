import uuid
import datetime
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
        result = self.get_task(uuid)

        if result['status'] == 'ok':
            current_task = result['document']
        else:
            return result

        current_status = current_task['status']
        current_status_history = current_task['status_history']
        current_date_status = current_task['date']
        current_log = current_task['log']

        new_status = task['status']
        new_date_status = datetime.datetime.now().time().isoformat()
        new_log = task['log']

        current_status_history.append( [ current_status, 
                                         current_date_status,
                                         current_log ] )

        current_task['status'] = new_status
        current_task['date'] = new_date_status
        current_task['log'] = new_log
        current_task['status_history'] = current_status_history

        return self.tasks_repository.update_task(uuid, current_task)

    def delete_task(self, name):
        return self.tasks_repository.delete_task(name)

    def delete_all_tasks(self):
        return self.tasks_repository.delete_all_tasks()