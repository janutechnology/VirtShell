API Calls Reference
===================

Start Instance
==============

Lets your start a instance

###Example###

`POST /api/virtshell/v1/instances/start_instance/:id`
--------------------------------------------

Start a instance

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://virtshell/api/v1/instances/start_instance/420aa3f0-8d96-11e5-8994-feff819cdc9f'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "start": "success" }
```

Stop Instance
=============

Lets your stop a instance

###Example###

`POST /api/virtshell/v1/instances/stop_instance/:id`
--------------------------------------------

Stop a instance

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://virtshell/api/v1/instances/stop_instance/420aa3f0-8d96-11e5-8994-feff819cdc9f'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "stop": "success" }
```

Restart instance
================

Lets your restart a instance

###Example###

`POST /api/virtshell/v1/instances/restart_instance/:id`
--------------------------------------------

Start a instance

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://virtshell/api/v1/instances/restart_instance/420aa3f0-8d96-11e5-8994-feff819cdc9f'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "restart": "success" }
```

Clone instance
==============

Lets your clone a instance

###Example###

`POST /api/virtshell/v1/instances/clone_instance/:id`
--------------------------------------------

Start a instance

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://virtshell/api/v1/instances/clone_instance/420aa3f0-8d96-11e5-8994-feff819cdc9f'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "clone": "success" }
```

Execute command
===============

Lets your execute a command in one or more instances

###Example###

`POST /api/virtshell/v1/instances/execute_command/`
--------------------------------------------

Execute command in many instances, combining names, patterns and tags.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "instances": [
          {"name": "database_server_01"},
          {"name": "transactional_server_co"},          
          {"pattern": "web_server*"},
          {"pattern": "grid_server_[1:5]"},
          {"tag": "web"}
        ],
        "command": "apt-get upgrade" }' \
  'http://localhost:8080/virtshell/api/v1/instances/execute_command/'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "execute_command": "success" }


Copy file
=========

Lets your copy a file o directory in one or more instances

###Example###

`POST /api/virtshell/v1/instances/copy_files/`
--------------------------------------------

Execute command in many instances, combining names, patterns and tags.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "path": "https://<host>:<port>/api/virtshell/v1/files/database_servers/msql/my.cnf",
        "destination": "$MYSQL_HOME/my.cnf"
        "instances": [
            {"name": "database_server_01"},
            {"name": "web_server*"},
            {"name": "grid_[1:5]"},
            {"name": "transactional_server_co"},
            {"tag": "web"}
        ] }' \
  'http://localhost:8080/virtshell/api/v1/instances/copy_files/'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "copy_files": "success" }
