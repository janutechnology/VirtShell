#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import tornado.ioloop
import pyrestful.rest

import virtshell_server_srv
from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete

class VirtShellServerAPI(pyrestful.rest.RestHandler):
    @post(_path="/host", 
          _types=[str,str,str,str,str,str,str,str,str,str], 
          _produces=mediatypes.APPLICATION_JSON)
    def create_host(self, **kwargs):
        return virtshell_server_srv.create_host(**kwargs)

if __name__ == '__main__':
    try:
        print("Start virtshell-server")
        app = pyrestful.rest.RestService([VirtShellServerAPI])
        app.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop virtshell-server")