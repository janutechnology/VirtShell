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

    def post(self, uuid=None, status=False, status_name=None):
        task = tornado.escape.json_decode(self.request.body)
        result = self.tasks.create_task(task)
        if result['status'] == 'ok':
            response = {"create": "success"}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None, status=False, status_name=None):
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


TasksResources = (r'/tasks/(.*)/status/(.*)', TasksHandler)