Packages API Reference
======================

Packages
========
Represents an individual package on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| install | POST | /packages/ | Install one or more packages. | 
| upgrade | PUT | /packages | Upgrade one or more packages. |
| remove | DELETE | /packages | Remove one or more packages. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "packages": [
      {"name": "package_name1"},
      {"name": "package_name2"}
  ],
  "instances": [ 
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

`POST /api/virtshell/v1/packages`
--------------------------------------------

Install one or more packages:

```sh
curl -sv -X POST \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "instances": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/install_packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "install_package": "in progress"
}
```

`PUT /api/virtshell/v1/packages`
--------------------------------------------

Upgrade one or more packages:

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "instances": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/upgrade_packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "upgrade_packages": "in progress"
}
```

`DELETE /api/virtshell/v1/packages`
--------------------------------------------

Remove one or more packages:

```sh
curl -sv -X DELETE \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "instances": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "remove_packages": "in progress"
}
```