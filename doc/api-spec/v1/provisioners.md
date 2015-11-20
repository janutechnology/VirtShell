Provisioners API Reference
==========================

Provisioners
============
Represents individual provisioner on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /provisioners/ | Inserts a new provisioner in the system. |
| list | GET | /provisioners | Retrieves the list of provisioners. |
| get | GET | /provisioners/id | Gets one provisioner by ID. |
| delete | DELETE | /provisioners/id | Deletes an existing provisioner. |
| update | PUT | /provisioners/id | Updates an existing provisioner. |

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
  "builder": "https://<host>:<port>/api/virtshell/v1/files/folder_name/director-backend.sh",
  "how_to_run": "java|python|sh|...",
  "tag": "backend",
  "depends": [ ... list of dependencies necessary for the builder ... ],
  "files": [ ... list of files necessary for the builder ... ],
  "templates": [ ... list of templates necessary for the builder ...],
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
       "builder": "https://<host>:<port>/api/virtshell/v1/files/builders/director-backend.sh",
       "how_to_run": "sh",
       "tag": "backend",
       "depends": [
            {"provisioner_name": "db-users", "version": "2.0.0"},
            {"provisioner_name": "db-transactional"}
        ],
       "files": [
            {"path": "https://<host>:<port>/api/virtshell/v1/files/queues/queue_mail_transform.py}
        ],
      "templates": [
            {"path": "https://<host>:<port>/api/virtshell/v1/files/queues/queue_mail_config.xml}
        ],        
       "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
       "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
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
      "uuid": "420a9fae-8d96-11e5-8994-feff819cdc9f",
      "name": "backend-services-provisioner",
      "builder": "https://<host>:<port>/api/virtshell/v1/files/builders/director-backend.sh",
      "how_to_run": "sh",
      "tag": "backend",
      "depends": [
          {"provisioner_name": "db-users", "version": "2.0.0"},
          {"provisioner_name": "db-transactional"}
      ],
      "files": [
          {"path": "https://<host>:<port>/api/virtshell/v1/files/queues/queue_mail_transform.py}
      ],
      "templates": [
          {"path": "https://<host>:<port>/api/virtshell/v1/files/queues/queue_mail_config.xml}
      ],        
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    },
    { 
      "uuid": "420a9fae-8d96-11e5-8994-feff819cdc9f",
      "name": "db-transactional",
      "builder": "https://<host>:<port>/api/virtshell/v1/files/databases/director-dbt.sh",
      "how_to_run": "sh",
      "tag": "dbt",        
      "created": {"at":"1429207233", "by":"420aa2c4-8d96-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    }    
  ]
}   
```

`GET /api/virtshell/v1/provisioners/:id
----------------------------------------------

Get a provisioner.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/provisioners/?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
  { 
    "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
    "name": "db-transactional",
    "builder": "https://<host>:<port>/api/virtshell/v1/files/databases/director-dbt.sh",
    "how_to_run": "sh",
    "tag": "dbt",        
    "created": {"at":"1429207233", "by":"420aa2c4-8d96-11e5-8994-feff819cdc9f"},
    "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
  }
```

`PUT /api/virtshell/v1/provisioners/:id`
----------------------------------------------

Update a existing provisioner.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "files": [
          {"path": "https://<host>:<port>/api/virtshell/v1/files/mysql/my.cnf}
      ]
  }' \
   'http://localhost:8080/api/virtshell/v1/provisioners?id=8de7b824-d7d1-4265-a3a6-5b46cc9b8ed5'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /api/virtshell/v1/provisioners/:id`
----------------------------------------------

Delete a existing provisioner.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/provisioners?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```