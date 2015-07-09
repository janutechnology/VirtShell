ISOs API Reference
==================

ISO
====
Represents an individual iso on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /isos/id | Gets one iso by ID. |
| list | GET | /isos | Retrieves the list of isos. |
| create | POST | /isos/id | Inserts a new host configuration. | 
| delete | DELETE | /isos/id | Deletes an existing iso. |
| update | PUT | /isos/id | Updates an existing iso. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
    "release_version": "version",
    "os": "systemoperating",
    "variant" : "server/desktop",
    "arch": "architecture",
    "timezone": "yourtimezone",
    "user" : "youruser",
    "password" : "yourpassword",
    "key" : "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABA...",
    "preseed_file" : "path"
}
```

###Examples###

`POST /api/virtsh/v1/isos`
--------------------------------------------

Create a new iso.

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{ "release_version": "14.04.2", 
		  "os": "ubuntu", 
		  "variant": "server", 
		  "arch": "amd64",
		  "timezone": "America/Bogota", 
		  "user": "janu", 
		  "password": "janu", 
		  "preseed_file": "my_seed_file.seed" }' \
   'http://localhost:8080/api/virtshell/v1/isos?id=Ubuntu14.04'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtsh/v1/isos/:id`
----------------------------------------------

`GET /api/virtsh/v1/isos/`
----------------------------------------------

`PUT /api/notify/v2/isos/:id`
----------------------------------------------

`DELETE /api/notify/v2/isos/:id`
----------------------------------------------