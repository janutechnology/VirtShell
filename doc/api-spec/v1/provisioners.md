Provisioners API Reference
==========================

Provisioners
============
Represents individual provisioner on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /provisioners/ | Creates a new provisioner in the system. |
| list | GET | /provisioners | Retrieves the list of provisioners. |
| get | GET | /provisioners/:name | Gets one provisioner by name. |
| delete | DELETE | /provisioners/:name | Deletes an existing provisioner. |
| update | PUT | /provisioners/:name | Updates an existing provisioner. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "backend-services-provisioner",
  "description": "Installs/Configures a backend server",
  "version": "1.5.8",
  "repository": "https://github.com/janutechnology/VirtShell_Provisioners_Examples.git",
  "executor": "run1.sh",
  "tag": "backend",
  "depends": [ ... list of dependencies necessary for the builder ... ],
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /api/virtshell/v1/provisioners`
--------------------------------------------

Create a new provisioner.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"name": "backend-services-provisioner",
       "repository": "https://github.com/janutechnology/VirtShell_Provisioners_Examples.git",
       "executor": "run1.sh",
       "tag": "backend",
       "depends": [
            {"provisioner_name": "db-users", "version": "2.0.0"},
            {"provisioner_name": "db-transactional"}
        ]
      }' \
   'http://localhost:8080/api/virtshell/v1/provisioners'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtshell/v1/provisioners/`
----------------------------------------------

Get all provisioners.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/provisioners'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "provisioners": [
    {
      "name": "backend-services-provisioner",
      "repository": "https://github.com/janutechnology/VirtShell_Provisioners_Examples.git",
      "executor": "run1.sh",
      "tag": "backend",
      "depends": [
          {"provisioner_name": "db-users", "version": "2.0.0"},
          {"provisioner_name": "db-transactional"}
      ]
    },
    {
      "name": "db-transactional",
      "repository": "https://github.com/janutechnology/VirtShell_Provisioners_Examples.git",
      "executor": "run_db.sh",
      "tag": "db"
    }
  ]
}
```

`GET /api/virtshell/v1/provisioners/:name
----------------------------------------------

Get a provisioner.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/provisioners/backend-services-provisioner'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
  {
    "name": "backend-services-provisioner",
    "repository": "https://github.com/janutechnology/VirtShell_Provisioners_Examples.git",
    "executor": "run1.sh",
    "tag": "backend",
    "depends": [
        {"provisioner_name": "db-users", "version": "2.0.0"},
        {"provisioner_name": "db-transactional"}
    ],
    "created": {"at":"1429207233", "by":"420aa2c4-8d96-11e5-8994-feff819cdc9f"},
    "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}    
  }
```

`PUT /api/virtshell/v1/provisioners/:name`
----------------------------------------------

Update an existing provisioner.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "executor": "run_backend.sh" }' \
   'http://localhost:8080/api/virtshell/v1/provisioners/backend-services-provisioner
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /api/virtshell/v1/provisioners/:name`
----------------------------------------------

Delete an existing provisioner.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/provisioners/backend-services-provisioner
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```