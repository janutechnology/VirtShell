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

import json
import sys

if sys.version_info > (3,):
	raw_input = input
	import http.client as httplib
	import urllib.parse as urllib
else:
	import httplib
	import urllib

print('Create host')
print('===============')
params  = urllib.urlencode({"name": "host-01-pdn",
							"os": "Ubuntu_12.04_3.5.0-23.x86_64",
							"memory": "16GB",
							"capacity": "120GB",
							"enabled": "true",
							"type" : "GeneralPurpose",
							"local_ipv4": "15.54.88.19",
							"local_ipv6": "ff06:0:0:0:0:0:0:c3",
							"public_ipv4": "10.54.88.19",
							"public_ipv6": "yt06:0:0:0:0:0:0:c3"})
headers = {"Content-Type": "application/x-www-form-urlencoded"}
conn    = httplib.HTTPConnection("localhost:8080")
conn.request('POST','/host',params,headers)

resp = conn.getresponse()
data = resp.read()
if resp.status == 200:
	json_data = json.loads(data.decode('utf-8'))
	print(json_data)
else:
	print(data)