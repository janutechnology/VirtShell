Properties API Reference
========================

Properties
==========
Represents an individual propertie on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /properties/ | Gets one or more propertie by instance name or tag. |


Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "properties": [
      {"name": "propertie_name1"},
      {"name": "propertie_name2"}
  ],
  "hosts": [ 
      {"name": "Host_", "range": "[1-3]"}, 
      {"name": "database_001"}
  ],
  "tags": [
    {"name": "db"},
    {"name": "web"}
  ]
}
```

###Examples###

`GET /api/virtshell/v1/properties/`
-----------------------------------

Get one or more properties of one instance.

```sh
curl -sv -X GET \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "properties": [{"name": "memory"}, {"name": "cpu"}],
        "hosts": [{"name": "WebServer"}]}' \
   'http://localhost:8080/api/virtshell/v1/properties'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "name": "WebServer",
  "memory": 1024,
  "cpu": 87.4
}
```

`GET /api/virtshell/v1/properties/`
-----------------------------------

Get one or more properties of one or more instances by tag.

```sh
curl -sv -X GET \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "properties": [{"name": "memory"}, {"name": "cpu"}],
        "tag": [{"name": "web"}]}' \
   'http://localhost:8080/api/virtshell/v1/properties'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  properties: [
    {
     "id": "kj5436c0-dc94-13tg-82ce-9992b5d5c51b",
     "name": "WebServerPhp001",
     "memory": 1024,
     "cpu": 2
    },
    {
     "id": "591b3828-7aaf-4833-a94c-ad0df44d59a4",
     "name": "WebServerPhp002",
     "memory": 1024,
     "cpu": 1  
    }
  ]
}
```

`GET /api/virtshell/v1/properties/`
-----------------------------------

Get one or more properties of one or more instances by host and range.

```sh
curl -sv -X GET \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "properties": [{"name": "memory"}, {"name": "cpu"}],
        {"name": "Database00", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/properties'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  properties: [
    {
     "id": "kj5436c0-dc94-13tg-82ce-9992b5d5c51b",
     "name": "Database001",
     "memory": 4024,
     "cpu": 2
    },
    {
     "id": "591b3828-7aaf-4833-a94c-ad0df44d59a4",
     "name": "Database002",
     "memory": 4024,
     "cpu": 1  
    },
    {
     "id": "f7c81039-5c88-423b-8b0d-c124483d586b",
     "name": "Database003",
     "memory": 4024,
     "cpu": 3  
    }
  ]  
}
```
