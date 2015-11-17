Instances API Reference
=======================

Instances
=========
Represents individual instance on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| create | POST | /instances/ | Create a new instances in any host. |
| list | GET | /instances | Retrieves the list of instances. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "username": "virtshell",
  "type": "system/regular",
  "login": "user@mail.com",
  "groups": [ {"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
              {"uuid": "a146d00c-8c90-11e5-8994-feff819cdc9f"}
  ],
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /virtshell/api/v1/users`
--------------------------------------------

Create a new user.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
    -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
       "username": "virtshell",
       "type": "system/regular",
       "login": "user@mail.com",
       "groups": [ {"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
                   {"uuid": "a146d00c-8c90-11e5-8994-feff819cdc9f"}
        ],
       "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
       "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
      }' \
   'http://localhost:8080/api/virtshell/v1/users'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /virtshell/api/v1/users/:id`
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
  "username": "virtshell",
  "type": "system/regular",
  "login": "user@mail.com",
  "groups": [ {"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"}],
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

`GET /virtshell/api/v1/users/`
----------------------------------------------

Get all users.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/users'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "users": [
      {
        "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
        "username": "virtshell",
        "type": "system",
        "login": "virtshell@mail.com",
        "groups": [ {"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
                   {"uuid": "a146d00c-8c90-11e5-8994-feff819cdc9f"}
        ],        
        "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
        "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
      },
      {
        "uuid": "1fcc7ee8-8c9d-11e5-8994-feff819cdc9f",
        "username": "demouser",
        "type": "regular",
        "login": "demo@gmail.com",
        "groups": [ {"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"}],        
        "created": {"at":"1431799233", "by":"1fcc8294-8c9d-11e5-8994-feff819cdc9f"},
        "modified": {"at":"1432836033", "by":"F2d31132-8c9c-11e5-D994-eeff819cdc9f"}
      }      
  ]
}   
```

`PUT /virtshell/api/v1/groups/:id`
----------------------------------------------

Update a existing user.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"type": "system",
       "groups": [{"uuid": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
                  {"uuid": "a146d00c-8c90-11e5-8994-feff819cdc9f"}]}' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=1fcc7ee8-8c9d-11e5-8994-feff819cdc9f'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /virtshell/api/v1/hosts/:id`
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