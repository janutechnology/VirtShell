import json
import logger
import tornado.web
import tornado.ioloop
from managment.tasks import Tasks

class StatusTasksHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.tasks = Tasks()
        self.logger = logger

    def get(self, status_name=None):
        self.logger.info("statustasks GET " + status_name)
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
    def initialize(self, logger):
        self.tasks = Tasks()
        self.logger = logger

    def get(self, uuid=None):
        self.logger.info("tasks GET " + str(uuid))
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
        self.logger.info("tasks POST " + str(uuid))
        task = tornado.escape.json_decode(self.request.body)
        result = self.tasks.create_task(task)
        if result['status'] == 'ok':
            response = {"create": "success", "task_id": result['uuid']}
        else:
            response = {"create": "error", "reason": result['reason']}
        return self.write(json.dumps(response))

    def put(self, uuid=None):
        self.logger.info("tasks PUT " + str(uuid))
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

    def delete(self, uuid=None):
        self.logger.info("tasks DELETE " + str(uuid))
        if uuid:
            result = self.tasks.delete_task(uuid)
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        else:
            result = self.tasks.delete_all_tasks()
            if result['status'] == 'ok':
                response = {"delete": "success"}
            else:
                response = {"delete": "error", "reason": result['reason']}
        return self.write(json.dumps(response))        

StatusTasksResources = (r'/tasks/status/(.*)', StatusTasksHandler)
TasksResources = (r'/tasks/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})*', TasksHandler)
