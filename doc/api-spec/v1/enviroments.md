Enviroments API Reference
=========================

Enviroments
===========
Collection of enviroments that relates one or more physical machines.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /enviroments/ | Creates a new enviroment. |
| list | GET | /enviroments | Retrieves the list of enviroments. |
| get | GET | /enviroments/:name | Gets one enviroments by name. |
| get | GET | /enviroments/:name/hosts/ | Gets all host of the one enviroments by name. |
| delete | DELETE | /enviroments/:name | Deletes an existing enviroment. |
| update | PUT | /enviroments/:name | Updates an existing enviroment. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "bigdata_test_01",
  "description": "Collection of servers oriented to big data.", 
  "users": [ ... list of users allowed to use the enviroment ...],
  "section": "section associated with the enviroment",
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /api/virtshell/v1/enviroments`
--------------------------------------------

Create a new enviroment.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
       "name": "bigdata_test_01",
       "description": "Collection of servers oriented to big data.", 
       "users": [ ... list of users allowed to use the enviroment ...],
       "section": "section associated with the enviroment",
       "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
       "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
      }' \
   'http://localhost:8080/api/virtshell/v1/enviroments'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "in progress" }
```

`GET /api/virtshell/v1/enviroments/`
----------------------------------------------

Get all enviroments.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/enviroments'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "enviroments": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "name": "bigdata_test_01",
      "description": "Collection of servers oriented to big data.", 
      "users": [ ... list of users allowed to use the enviroment ...],
      "section": "section associated with the enviroment",
      "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
      "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
    },
    { 
      "uuid": "efa1777c-cad7-11e5-9956-625662870761",
      "name": "backend_development",
      "description": "All backend of the company", 
      "users": [ ... list of users allowed to use the enviroment ...],
      "section": "section associated with the enviroment",      
      "created": {"at":"1429207233", "by":"1a900cdc-cad8-11e5-9956-625662870761"},
      "modified": {"at":"1529207233", "by":"2163b554-cad8-11e5-9956-625662870761"}
    }    
  ]
}   
```

`GET /api/virtshell/v1/enviroments/:name
----------------------------------------------

Get an enviroments.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/enviroments/backend_development'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "uuid": "efa1777c-cad7-11e5-9956-625662870761",
  "name": "backend_development",
  "description": "All backend of the company", 
  "users": [ ... list of users allowed to use the enviroment ...],
  "section": "section associated with the enviroment",
  "created": {"at":"1429207233", "by":"1a900cdc-cad8-11e5-9956-625662870761"},
  "modified": {"at":"1529207233", "by":"2163b554-cad8-11e5-9956-625662870761"}
}
```

`GET /api/virtshell/v1/enviroments/:name/section
------------------------------------------------

Get the section associated to the enviroment.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/enviroments/backend_development/section'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "section": "section associated with the enviroment",  
}
```

`DELETE /api/virtshell/v1/enviroments/:name`
----------------------------------------------

Delete an existing enviroment.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/enviroments/backend_development'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```