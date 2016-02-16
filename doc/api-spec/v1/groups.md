Groups API Reference
====================

Groups
====
Represents individual groups on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /groups/:name | Gets one group by ID. |
| list | GET | /groups | Retrieves the list of groups. |
| create | POST | /groups/ | Inserts a new group configuration. | 
| delete | DELETE | /groups/:name | Deletes an existing group. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "web_development_team",
  "users": [ ... list of members of the group ...],
  "created":[ {"at":"timestamp"}, {"by":user_id}]
}
```

###Examples###

`POST /api/virtshell/v1/groups`
--------------------------------------------

Create a new group.

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
    -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "name": "web_development_team" }' \
   'http://localhost:8080/api/virtshell/v1/groups'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtshell/v1/groups/:name`
----------------------------------------------

Get a group by name.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/groups/web_development_team'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "web_development_team",
  "users": [ 
      {"username": "user1", "id": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
      {"username": "user2", "id": "a146d00c-8c90-11e5-8994-feff819cdc9f"}
  ]
  "created":[{"at":"1447696674"}, {"by":"a379e8e6-8c8b-11e5-8994-feff819cdc9f"}]
}
```

`GET /api/virtshell/v1/groups/`
----------------------------------------------

Get all groups.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/groups'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "groups": [
    {
      "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
      "name": "web_development_team",
      "users": [ 
          {"username": "user1", "id": "a146cae4-8c90-11e5-8994-feff819cdc9f"},
          {"username": "user2", "id": "a146d00c-8c90-11e5-8994-feff819cdc9f"}
      ],     
      "created":[{"at":"1447696833"}, {"by":"d2372efa-8c8b-11e5-8994-feff819cdc9f"}]
    },
    {
      "uuid": "a379f19c-8c8b-11e5-8994-feff819cdc9f",
      "name": "math_team",
      "users": [ 
          {"username": "user3", "id": "a146cae4-8c90-11e5-8994-feff819cdc9f"}
      ],     
      "created":[{"at":"1421431233"}, {"by":"18489280-8c91-11e5-8994-feff819cdc9f"}]
    },
    {
      "uuid": "a379f3d6-8c8b-11e5-8994-feff819cdc9f",
      "name": "chemical_team",
      "users": [ 
          {"username": "user4", "id": "F8489280-8c91-11e5-8994-feff819cdc9f"},
          {"username": "user5", "id": "18489780-8c91-11e5-8994-feff819cdc9f"}
      ],       
      "created":[{"at":"1424109633"}, {"by":"d2373576-8c8b-11e5-8994-feff819cdc9f"}]
    },        
}   
```

`DELETE /api/virtshell/v1/groups/:name`
----------------------------------------------
Delete an existing group.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://localhost:8080/api/virtshell/v1/groups/chemical_team'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```