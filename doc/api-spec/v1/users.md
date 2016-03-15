Users API Reference
===================

Users
=====
Represents individual user on VirtShell.


| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /users/:name | Gets one user by name. |
| create | POST | /users/ | Inserts a new user in the system. |
| list | GET | /users | Retrieves the list of users. | 
| delete | DELETE | /users/:name | Deletes an existing user. |
| update | PUT | /users/:name | Updates an existing user. |

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
  "groups": [ {"name": "web_development_team"},
              {"name": "production"}
  ],
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

###Examples###

`POST /api/virtshell/v1/users`
--------------------------------------------

Create a new user.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{
       "username": "virtshell",
       "type": "system/regular",
       "login": "user@mail.com",
       "groups": [ 
                  {"name": "web_development_team"},
                  {"name": "production"}
                 ]
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

`GET /api/virtshell/v1/users/`
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
        "groups": [ {"name": "web_development_team"},
                    {"name": "production"}
        ],        
        "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
        "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
      },
      {
        "uuid": "1fcc7ee8-8c9d-11e5-8994-feff819cdc9f",
        "username": "demouser",
        "type": "regular",
        "login": "demo@gmail.com",
        "groups": [ {"name": "production"}],
        "created": {"at":"1431799233", "by":"1fcc8294-8c9d-11e5-8994-feff819cdc9f"},
        "modified": {"at":"1432836033", "by":"F2d31132-8c9c-11e5-D994-eeff819cdc9f"}
      }      
  ]
}   
```

`GET /api/virtshell/v1/users/:name
----------------------------------------------

Get an user by nam.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://<host>:<port>/api/virtshell/v1/users/virtshell'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "username": "virtshell",
  "type": "system",
  "login": "virtshell@mail.com",
  "groups": [ {"name": "web_development_team"},
              {"name": "production"}
  ],        
  "created": {"at":"1429207233", "by":"92d30f0c-8c9c-11e5-8994-feff819cdc9f"},
  "modified": {"at":"1529207233", "by":"92d31132-8c9c-11e5-8994-feff819cdc9f"}
}
```

`DELETE /api/virtshell/v1/users/:name`
----------------------------------------------

Delete an existing user.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/users/virtshell'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }


`PUT /api/virtshell/v1/users/:name`
----------------------------------------------

Update an existing user.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
    -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{"type": "user"}' \
   'http://localhost:8080/api/virtshell/v1/users/virtshell'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```