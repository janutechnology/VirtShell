Packages API Reference
======================

Packages
========
Represents an individual package on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| install | POST | /install_packages/ | Install one or more packages. | 
| upgrade | POST | /upgrade_packages | Upgrade one or more packages. |
| remove | POST | /remove_packages | Remove one or more packages. |

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

`POST /api/virtshell/v1/install_package`
--------------------------------------------

Install one or more packages:

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "hosts": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/install_packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "install_package": "accepted"
}
```

`POST /api/virtshell/v1/upgrade_packages`
--------------------------------------------

Upgrade one or more packages:

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "hosts": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/upgrade_packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "upgrade_packages": "accepted"
}
```

`POST /api/virtshell/v1/remove_packages`
--------------------------------------------

Remove one or more packages:

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H "Content-Type: text/plain" \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -d '{ "packages": [{"name": "git"}, {"name": "nginx"}],
        "hosts": [{"name": "WebServer_", "range": "[1-3]"}]}' \
   'http://localhost:8080/api/virtshell/v1/remove_packages'
```

Response:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
```
```json
{ 
  "remove_packages": "accepted"
}
```