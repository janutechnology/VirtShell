import tornado.ioloop
import tornado.web

import managment
import config as CONFIG
from managment.hosts_api import HostsResources
from security.users_api import UsersResources
from security.groups_api import GroupsResources
from provisioning.provisioners_api import ProvisionersResources
from managment.instances_api import InstancesResources
from managment.partitions_api import PartitionsResources
from managment.enviroments_api import EnviromentsResources

def main(debug = True, port = CONFIG.PORT):
    try:
        print("Start virtshell-server")
        application = tornado.web.Application([HostsResources, 
                                               UsersResources,
                                               GroupsResources,
                                               ProvisionersResources,
                                               InstancesResources,
                                               EnviromentsResources,
                                               PartitionsResources], 
                                              debug = debug, 
                                              autoreload = debug)
        application.listen(port)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nStop virtshell-server")        

if __name__ == '__main__':
    main()    
