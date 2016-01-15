Hosts API Reference
===================

Host
====
Represents an individual host on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /hosts/id | Gets one host by ID. |
| list | GET | /hosts | Retrieves the list of hosts. |
| create | POST | /hosts/ | Inserts a new host configuration. | 
| delete | DELETE | /hosts/id | Deletes an existing host. |
| update | PUT | /hosts/id | Updates an existing host. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "host-01-pdn",
  "os": "Ubuntu_12.04_3.5.0-23.x86_64",
  "memory": "16GB",
  "capacity": "120GB",
  "enabled": "true|false",
  "type" : "StorageOptimized|GeneralPurpose|HighPerformance",
  "local_ipv4": "15.54.88.19",
  "local_ipv6": "ff06:0:0:0:0:0:0:c3",
  "public_ipv4": "10.54.88.19",
  "public_ipv6": "yt06:0:0:0:0:0:0:c3",
  "instances": [
    ... instances resource is here
  ],
  "created":["at":"timestamp", "by":user_id]
}
```

###Examples###

`POST /api/virtshell/v1/hosts`
--------------------------------------------

Create a new host.

```sh
curl -sv -X POST \
	-H 'accept: application/json' \
   	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{"name": "host-01-pdn",
  		 "os": "Ubuntu_12.04_3.5.0-23.x86_64",
  		 "memory": "16GB",
  		 "capacity": "120GB",
  		 "enabled": "true",
  		 "type" : "GeneralPurpose",
  		 "local_ipv4": "15.54.88.19",
  	     "local_ipv6": "ff06:0:0:0:0:0:0:c3",
  		 "public_ipv4": "10.54.88.19",
  		 "public_ipv6": "yt06:0:0:0:0:0:0:c3"}' \
   'http://localhost:8080/api/virtshell/v1/hosts'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success", "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b"}
```

`GET /api/virtshell/v1/hosts/:id`
----------------------------------------------

Get a host.

```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://localhost:8080/api/virtshell/v1/hosts?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "host-01-pdn",
  "os": "Ubuntu_12.04_3.5.0-23.x86_64",
  "memory": "16GB",
  "capacity": "120GB",
  "enabled": "true",
  "type" : "StorageOptimized",
  "local_ipv4": "15.54.88.19",
  "local_ipv6": "ff06:0:0:0:0:0:0:c3",
  "public_ipv4": "10.54.88.19",
  "public_ipv6": "yt06:0:0:0:0:0:0:c3",
  "instances": [
		{
			"name": "name1",
			"id": "72C05559-0590-4DA6-BE56-28AB36CB669C"
		},
		{
			"name": "name2",
			"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
		}
  ],
  "created":["at":"20130625105211", "by":10]
}
```

`GET /api/virtshell/v1/hosts/`
----------------------------------------------

Get all host.

```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://localhost:8080/api/virtshell/v1/hosts'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
	"hosts": [
		{
			"uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
			"name": "host-01-pdn",
			"os": "Ubuntu_12.04_3.5.0-23.x86_64",
			"memory": "16GB",
			"capacity": "120GB",
			"enabled": "true",
			"type" : "StorageOptimized",
			"local_ipv4": "15.54.88.19",
			"local_ipv6": "ff06:0:0:0:0:0:0:c3",
			"public_ipv4": "10.54.88.19",
			"public_ipv6": "yt06:0:0:0:0:0:0:c3",
			"instances": [
				{
					"name": "name1",
					"id": "72C05559-0590-4DA6-BE56-28AB36CB669C"
				},
				{
					"name": "name2",
					"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
				}
			],
			"created":["at":"20130625105211", "by":10]
		},
		{
			"uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
			"name": "host-01-pdn",
			"os": "Ubuntu_12.04_3.5.0-23.x86_64",
			"memory": "16GB",
			"capacity": "120GB",
			"enabled": "true",
			"type" : "GeneralPurpose",
			"local_ipv4": "15.54.88.19",
			"local_ipv6": "ff06:0:0:0:0:0:0:c3",
			"public_ipv4": "10.54.88.19",
			"public_ipv6": "yt06:0:0:0:0:0:0:c3",
			"instances": [
				{
					"name": "name3",
					"id": "DE11CC9A-482F-4033-A7F8-503EE449DD0A"
				},
				{
					"name": "name4",
					"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
				},		
			],
			"created":["at":"20130625105211", "by":10]
		}
	]
}		
```

`PUT /api/virtshell/v1/hosts/:id`
----------------------------------------------

Update a existing host.

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
   	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{"memory": "24GB",
		 "capacity": "750GB"}' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /api/virtshell/v1/hosts/:id`
----------------------------------------------
Delete a existing host.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```