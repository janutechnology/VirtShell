import logger
import tornado.web
import tornado.ioloop
import config
from security.users_api import UsersResources
from managment.tasks_api import TasksResources
from managment.hosts_api import HostsResources
from security.groups_api import GroupsResources
from managment.tasks_api import StatusTasksResources
from managment.instances_api import InstancesResources
from managment.partitions_api import PartitionsResources
from managment.enviroments_api import EnviromentsResources
from managment.partitions_api import PartitionsHostResources
from provisioning.provisioners_api import ProvisionersResources

def get_handlers(log):
  handlers_without_arguments = [HostsResources, 
                                UsersResources,
                                GroupsResources,
                                ProvisionersResources,
                                InstancesResources,
                                EnviromentsResources,
                                PartitionsResources,
                                PartitionsHostResources,
                                TasksResources,
                                StatusTasksResources]

  logger_argument = (dict(logger=log), )
  handlers_with_arguments = []
  for handler in handlers_without_arguments:
    handler += logger_argument
    handlers_with_arguments.append(handler)

  return handlers_with_arguments

def main(debug = True, port = config.PORT):
  try:
    log = logger.get_logger('virtshell_server')
    log.info("server started...")  

    handlers = get_handlers(log)

    application = tornado.web.Application(handlers,
                                          debug = debug, 
                                          autoreload = debug)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
  except KeyboardInterrupt:
    log.info("server stoped...")       

if __name__ == '__main__':
  main(debug = False)    
