from pymongo import MongoClient
from bson.objectid import ObjectId

CLIENT = MongoClient("mongodb://localhost:27017")
mongodb = CLIENT.virtshell_server
for host in mongodb.hosts.find():
	print (host)

new_host = {"uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
			"name": "host-01-pdn",
			"os": "Ubuntu_12.04_3.5.0-23.x86_64",
			"memory": "16GB",
			"capacity": "120GB",
			"enabled": "true",
			"type" : "GeneralPurpose",
			"local_ipv4": "15.54.88.19",
			"local_ipv6": "ff06:0:0:0:0:0:0:c3",
			"public_ipv4": "10.54.88.19",
			"public_ipv6": "yt06:0:0:0:0:0:0:c3"}

host_id = mongodb.hosts.insert_one(new_host).inserted_id
print(type(host_id))
if isinstance(host_id, ObjectId):
	print("kkkkk")
print(host_id)

for host in mongodb.hosts.find():
	print (host)

