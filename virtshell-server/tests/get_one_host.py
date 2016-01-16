# -*- coding: utf-8 -*-

import sys
import json

if sys.version_info > (3,):
        raw_input = input
        import http.client as httplib
        import urllib.parse as urllib
else:
        import httplib
        import urllib


print('Get one host')
print('=============')

headers = {"Content-type": "application/x-www-form-urlencoded"}
conn    = httplib.HTTPConnection("localhost:8080")

uuid = '37c31772-63a6-4668-8992-5eac36f694f8'

conn.request('GET','/hosts/%s'%uuid)

resp = conn.getresponse()
data = resp.read()
if resp.status == 200:
	json_data = json.loads(data.decode('utf-8'))
	print(json_data)
else:
	print(data.decode('utf-8'))