import tornado.ioloop
import tornado.web

import indico.config as CONFIG
from virtshell_server.resources.hosts import HostsResource

def main(debug = True, port = CONFIG.PORT):
	try:
		print("Start virtshell-server")
	    application = tornado.web.Application([
	        HostsResource
	    ], debug = debug
	     , autoreload = debug)

	    application.listen(port)
	    tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nStop virtshell-server")	    

if __name__ == '__main__':
	main()    
