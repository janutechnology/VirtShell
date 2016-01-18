import tornado.ioloop
import tornado.web

import managment
import config as CONFIG
from managment.hosts_api import HostsResources

def main(debug = True, port = CONFIG.PORT):
    try:
        print("Start virtshell-server")
        application = tornado.web.Application([HostsResources], 
                                              debug = debug, 
                                              autoreload = debug)
        application.listen(port)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nStop virtshell-server")        

if __name__ == '__main__':
    main()    
