Tasks API Reference
===================

Tasks
=====
Represents an individual task on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /tasks/ | Gets all tasks. |
| get | GET | /tasks/:id | Gets one task by ID. |
| get | GET | /tasks/status/:status | Gets all task by status name. |
| create | POST | /tasks/ | Creates a new task. | 
| update | PUT | /tasks/:id | Updates an existing task. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "description": "clone virtual machine database_01",
  "status" : "pending|in progress|sucess|failed",
  "type": "create_instance|delete_instance|restart_instance|...",
  "object_uuid": "uuid of the object (instance, host, property, ...)",
  "created":["at":"timestamp", "by":user_id],
  "last_update": "timestamp",
  "log": "summary of the task"
}
```

###Examples###

`GET /api/virtshell/v1/tasks/
----------------------------------------------

Get the information of all tasks.


```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/tasks/'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "tasks": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "description": "clone virtual machine database_01",
      "status" : "in progress",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "last_update": "1429207435",
      "log": "summary of the task"
    },
    {
      "uuid": "a62ad146-ccf4-11e5-9956-625662870761",
      "description": "create container webserver_09",
      "status" : "sucess",
      "created": {"at":"1454433171", "by":"cc7f8e2c-ccf4-11e5-9956-625662870761"},
      "last_update": "1454436771",
      "log": "summary of the task"
    }
  ]
}  
```

`GET /api/virtshell/v1/tasks/:id
----------------------------------------------

Get the information of one task by id.


```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://<host>:<port>/api/virtshell/v1/tasks/ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "description": "clone virtual machine database_01",
  "status" : "in progress",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "last_update": "1429207435",
  "log": "summary of the task"
}
```

`GET /api/virtshell/v1/tasks/:status
----------------------------------------------

Get the information of all tasks by status


```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/tasks/sucess'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "tasks": [
    {
      "uuid": "a62ad146-ccf4-11e5-9956-625662870761",
      "description": "create container webserver_09",
      "status" : "sucess",
      "created": {"at":"1454433171", "by":"cc7f8e2c-ccf4-11e5-9956-625662870761"},
      "last_update": "1454436771",
      "log": "summary of the task"
    }
  ]
}  
```

###Examples###

`POST /api/virtshell/v1/tasks`
--------------------------------------------

Create a new task.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
    -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "description": "clone virtual machine database_01",
        "status" : "in progress"}' \
   'http://localhost:8080/api/virtshell/v1/tasks'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success"}
```

`PUT /api/virtshell/v1/tasks/:id`
----------------------------------------------

Update an existing host.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
    -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"status": "sucess",
     "log": "....."}' \
   'http://localhost:8080/api/virtshell/v1/hosts/a62ad146-ccf4-11e5-9956-625662870761'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```