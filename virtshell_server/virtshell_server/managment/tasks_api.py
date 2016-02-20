import json
import tornado.web
import tornado.ioloop
from managment.tasks import Tasks

class StatusTasksHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.tasks = Tasks()

    def get(self, status_name=None):
        if status_name:
            result = self.tasks.get_tasks_by_status(status_name)
            if result['status'] == 'ok':
                tasks = result['documents']
                response = {'tasks': tasks}
            else:
                response = {'error': result['reason']}
        else:
            response = {"tasks_by_status": "error", "reason": "missing status name parameter"}
        return self.write(json.dumps(response))

class TasksHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.tasks = Tasks()

    def get(self, uuid=None):
        if uuid:
            result = self.tasks.get_task(uuid)
            if result['status'] == 'ok':
                response = result['document']
            else:
                response = {'error': result['reason']}
        else:
            result = self.tasks.get_all_tasks()
            if result['status'] == 'ok':
                tasks = result['documents']
                response = {'tasks': tasks}
            else:
                response = {'error': result['reason']}
        return self.write(json.dumps(response))

    def post(self, uuid=None):
        task = tornado.escape.json_decode(self.request.body)
        result = self.tasks.create_task(task)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        if uuid:
            task = tornado.escape.json_decode(self.request.body)
            result = self.tasks.update_task(uuid, task)
            if result['status'] == 'ok':
                response = {"update": "success"}
            else:
                response = {"update": "error", "reason": result['reason']}
        else:
            response = {"update": "error", "reason": "missing uuid parameter"}
        return self.write(json.dumps(response))

StatusTasksResources = (r'/tasks/status/(.*)', StatusTasksHandler)
TasksResources = (r'/tasks/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})*', TasksHandler)
