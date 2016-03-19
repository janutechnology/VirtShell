Instances API Reference
=======================

Instances
=========
Represents individual instance on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /instances/ | Creates a new instance within an enviroment. |
| list | GET | /instances | Retrieves the list of instances. |
| get | GET | /instances/:name | Gets one instance by ID. |
| delete | DELETE | /instances/:name | Deletes an existing instance. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "transactional_log",
  "memory": 1024,
  "cpus": 2,
  "hdsize": "2GB",
  "description": "Server transactional only for store logs", 
  "enviroment": "Enviroment name to which it belongs",
  "operating_system": "ubuntu_server_14.04.2_amd64",
  "provisioner": "all_backend",
  "permissions": "xwrxwrxwr",
  "host_type": "GeneralPurpose | ComputeOptimized | MemoryOptimized | StorageOptimized",
  "ipv4": "172.16.56.104",
  "ipv6": "FE80:0000:0000:0000:0202:B3FF:FE1E:8329",
  "driver": "lxc | virtualbox | vmware | ec2 | kvm | docker",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /api/virtshell/v1/instances`
--------------------------------------------

Create a new instance.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "name": "transactional_log",
        "memory": 1024,
        "cpus": 2,
        "hdsize": "2GB",
        "enviroment": "development_co", 
        "operating_system": "ubuntu_server_14.04.2_amd64",
        "description": "Server transactional only for store logs", 
        "provisioner": "all_backend",
        "host_type": "GeneralPurpose",
        "driver": "lxc"
      }' \
   'http://localhost:8080/api/virtshell/v1/instances'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "in progress" }
```

`GET /api/virtshell/v1/instances/`
----------------------------------------------

Get all instances.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/instances'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "instances": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "name": "transactional_log",
      "memory": 1024,
      "cpus": 2,
      "hdsize": "2GB",
      "operating_system": "ubuntu_server_14.04.2_amd64",
      "description": "Server transactional only for store logs", 
      "provisioner": "all_backend",
      "host_type": "GeneralPurpose",
      "enviroment": "development_co", 
      "drive": "lxc",
      "permissions": "xwrxwrxwr",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"cf744732-8f12-11e5-8994-feff819cdc9f"}
    },
    { 
      "uuid": "cf744476-8f12-11e5-8994-feff819cdc9f",
      "name": "orders_colombia",
      "memory": 2024,
      "cpus": 2,
      "hdsize": "4GB",
      "operating_system": "ubuntu_server_14.04.2_amd64",
      "description": "Server transactional dedicated to receive orders", 
      "provisioner": "orders_admin",
      "host_type": "StorageOptimized",
      "enviroment": "development_mx",
      "drive": "docker",
      "permissions": "xwrxwrxwr",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    }    
  ]
}   
```

`GET /api/virtshell/v1/instances/:name
----------------------------------------------

Get an instance.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/instances/orders_colombia'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "transactional_log",
  "memory": 1024,
  "cpus": 2,
  "hdsize": "2GB",
  "operating_system": "ubuntu_server_14.04.2_amd64",
  "description": "Server transactional only for store logs", 
  "provisioner": "all_backend",
  "host_type": "GeneralPurpose",
  "drive": "lxc",
  "permissions": "xwrxwrxwr",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"cf744732-8f12-11e5-8994-feff819cdc9f"}
  }
```


`DELETE /api/virtshell/v1/instances/:name`
----------------------------------------------

Delete an existing instance.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/instances/orders_colombia'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "in progress" }
```