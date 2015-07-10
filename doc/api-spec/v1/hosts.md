Hosts API Reference
===================

Host
====
Represents an individual host on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /hosts/id | Gets one host by ID. |
| list | GET | /hosts | Retrieves the list of hosts. |
| create | POST | /hosts/id | Inserts a new host configuration. | 
| delete | DELETE | /hosts/id | Deletes an existing host. |
| update | PUT | /hosts/id | Updates an existing host. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
    "ip": "anything",
    "user": "your user",
    "password" : "your_password",
    "key": "your_public_key",
    "type": "host_type"
}
```

###Examples###

`POST /api/virtsh/v1/hosts`
--------------------------------------------

Create a new host.

```sh
curl -sv -X POST \
	-H 'accept: application/json' \
   	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{ "ip": "192.168.56.77", 
		  "user": "janu", 
		  "password": "janu", 
		  "type": "GeneralPurpose" }' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=robot'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

```sh
curl -sv -X POST \
	-H 'accept: application/json' \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{ "ip": "192.168.56.77", 
		  "user": "janu", 
		  "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABA...", 
		  "type": "StorageOptimized" }' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=robot2'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtsh/v1/hosts/:id`
----------------------------------------------

Get a host.

```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://localhost:8080/api/virtshell/v1/hosts?id=robot2'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
	"ip": "192.168.56.77", 
	"user": "janu", 
	"type": "StorageOptimized",
	"added": {
	    "at": 1402954323,
	    "by": "UserId"
	},
	"instances": [
		{
			"name": "name1",
			"id": "72C05559-0590-4DA6-BE56-28AB36CB669C"
		},
		{
			"name": "name2",
			"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
		},		
	]
}
```

`GET /api/virtsh/v1/hosts/`
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
			"ip": "192.168.56.77", 
			"user": "janu", 
			"type": "StorageOptimized",
			"added": {
			    "at": 1402954323,
			    "by": "UserId"
			},
			"instances": [
				{
					"name": "name1",
					"id": "72C05559-0590-4DA6-BE56-28AB36CB669C"
				},
				{
					"name": "name2",
					"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
				},		
			]
		},
		{
			"ip": "192.168.56.78", 
			"user": "janu", 
			"type": "GeneralPurpose",
			"added": {
			    "at": 1502954323,
			    "by": "UserId"
			},
			"instances": [
				{
					"name": "name3",
					"id": "DE11CC9A-482F-4033-A7F8-503EE449DD0A"
				},
				{
					"name": "name4",
					"id": "17173587-C4E9-4369-9C43-FCBF5E075973"
				},		
			]
		}
	]
}		
```

`PUT /api/notify/v2/hosts/:id`
----------------------------------------------

Update a existing host.

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
   	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{ "ip": "192.168.56.77", 
		  "user": "janu", 
		  "password": "janu", 
		  "type": "GeneralPurpose" }' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=robot'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /api/notify/v2/hosts/:id`
----------------------------------------------
Delete a existing host.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=robot'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```