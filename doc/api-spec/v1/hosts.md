Hosts
=====
For Accounts Resource details, see the resource representation page.

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /hosts/id | Gets one host by ID. |
| list | GET | /hosts | Retrieves the list of hosts. |
| create | POST | /hosts/id | Inserts a new host configuration. | 
| delete | DELETE | /hosts/id | Deletes an existing host. |
| update | PUT | /hosts/id | Updates an existing host. |

Resource representations
========================
```json
{
    "ip": "anything",
    "user": "your user",
    "password" : "your_password",
    "key": "your_public_key",
    "type": "host_type"
}
```

###Examples###

`POST /api/virtsh/v1/hosts`
--------------------------------------------

Create a new host.

```sh
curl -sv -X PUT -d '{ "ip": "Jack", "last": "Sparrow" }' \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://localhost:8080/api/virtshell/v1/hosts?id=robot'
```


Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtsh/v1/hosts/:id`
----------------------------------------------

`GET /api/virtsh/v1/hosts/`
----------------------------------------------

`PUT /api/notify/v2/alerts/:id`
----------------------------------------------

`DELETE /api/notify/v2/alerts/:id`
----------------------------------------------