import json
import tornado.web
import tornado.ioloop
from managment.tasks import Tasks

class TasksHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.tasks = Tasks()

    def get(self, uuid=None, status=False, status_name=None):
        if not uuid and not status and not status_name:
            result = self.tasks.get_all_tasks()
        elif uuid and not status and not status_name: 
            result = tasks.get_task(uuid)
        elif not uuid and status and status_name:
            result = tasks.get_all_tasks_by_status(status_name)
        else:
            response = {'error': 'bad_request'}

        if result['status'] == 'ok':
            response = result['tasks']
        else:
            response = {'error': result['reason']}
        return self.write(json.dumps(response))

TasksResources = (r'/tasks/(.*)/status/(.*)', TasksHandler)