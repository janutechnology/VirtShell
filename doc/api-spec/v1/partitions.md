Partitions API Reference
========================

Partitions
==========
The partitions allow you to group physical machines in a specific policy areas.

| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /partitions/ | Creates a new partition. |
| list | GET | /partitions | Retrieves the list of partitions. |
| get | GET | /partitions/:name | Gets one partition by name. |
| get | GET | /partitions/:name/hosts/ | Gets all host of the one partition by name. |
| delete | DELETE | /partitions/:name | Deletes an existing partition. |
| update | PUT | /partitions/:name/host/:hostname | Add a host to partition. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "development_co",
  "description": "Collection of servers oriented to development team in Colombia.", 
  "hosts": [ ... list of hosts associated with the partition ...],
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /api/virtshell/v1/partitions`
--------------------------------------------

Create a new partition.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{
       "name": "development_co",
       "description": "Collection of servers oriented to development team in colombia."
      }' \
   'http://localhost:8080/api/virtshell/v1/partitions'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtshell/v1/partitions/`
----------------------------------------------

Get all partitions.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/partitions'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "partitions": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "name": "development_co",
      "description": "Collection of servers oriented to development team in colombia.",
      "hosts": [ ... list of hosts associated with the section ...],
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    },
    { 
      "uuid": "efa1777c-cad7-11e5-9956-625662870761",
      "name": "production_us_miami",
      "description": "Collection of servers oriented to production in us.",
      "hosts": [ ... list of hosts associated with the section ...],      
      "created": {"at":"1429207233", "by":"1a900cdc-cad8-11e5-9956-625662870761"},
      "modified": {"at":"1529207233", "by":"2163b554-cad8-11e5-9956-625662870761"}
    }    
  ]
}   
```

`GET /api/virtshell/v1/partitions/:name
----------------------------------------------

Get an partitions.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/partitions/development_co'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "uuid": "efa1777c-cad7-11e5-9956-625662870761",
  "name": "backend_development_04",
  "description": "Servers for backend of the company", 
  "hosts": [ ... list of hosts associated with the section ...],  
  "created": {"at":"1429207233", "by":"1a900cdc-cad8-11e5-9956-625662870761"},
  "modified": {"at":"1529207233", "by":"2163b554-cad8-11e5-9956-625662870761"}
}
```

`GET /api/virtshell/v1/partitions/:name/hosts
----------------------------------------------

Get the hosts associated to the partitions.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/partitions/backend_development_04/hosts'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "hosts": [ ... list of hosts associated with the section ...],  
}
```

`DELETE /api/virtshell/v1/partitions/:name`
----------------------------------------------

Delete an existing partition.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/partitions/backend_development_04'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```

`PUT /api/virtshell/v1/partitions/:name/host/:hostname`
-----------------------------------------------------

Add a host to partition.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  'http://localhost:8080/virtshell/api/v1/partitions/:name/host/:hostname'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "add_host": "success" }