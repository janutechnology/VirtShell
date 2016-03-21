Images API Reference
====================

Image
=====
Represents an individual image on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /image/:name | Gets one image by name. |
| list | GET | /image | Retrieves the list of images. |
| create | POST | /image/:name | Inserts a new image. | 
| delete | DELETE | /image/:name | Deletes an existing image. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
  "id": "kj5436c0-dc94-13tg-82ce-9992b5d5c51b",
  "name": "ubuntu_server_14.04.2_amd64",
  "type": "iso|lxc-container|docker-container",
  "os": "ubuntu", 
  "timezone": "America/Bogota",
  "permissions": "xwrxwrxwr",
  "ssh_key": "-------- BEGIN PUBLIC KEY ----and a valid key here",
  "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu14-04.txt",
  "download_url": "http://releases.ubuntu.com/raring/ubuntu-14.04-server-amd64.iso",
  "created":["at":"20130625105211","by":10],
  "details": "...."
}
```

###Examples###

`POST /api/virtshell/v1/images`
--------------------------------------------

Create a new image type iso.

```sh
curl -sv -X PUT \
	-H 'accept: application/json' \
	-H "Content-Type: text/plain" \
	-H 'X-VirtShell-Authorization: UserId:Signature' \
	-d '{"name": "ubuntu_server_14.04.2_amd64",
		 "type": "iso",
		 "os": "ubuntu",
		 "timezone": "America/Bogota", 
		 "key": "/home/callanor/.ssh/id_rsa.pub",
		 "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu14-04.txt",
     "download_url": "http://releases.ubuntu.com/raring/ubuntu-14.04-server-amd64.iso"}' \
   'http://localhost:8080/api/virtshell/v1/image'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "create": "success" }
```

`GET /api/virtshell/v1/images/:ubuntu_server_14.04.2_amd64`
----------------------------------------------

Get an image.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/images/ubuntu_server_14.04.2_amd64'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "id": "kj5436c0-dc94-13tg-82ce-9992b5d5c51b",
  "name": "ubuntu_server_14.04.2_amd64",
  "type": "iso",
  "os": "ubuntu",
  "permissions": "xwrxwrxwr",
  "timezone": "America/Bogota", 
  "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu_14_04.txt",
  "download_url": "http://releases.ubuntu.com/raring/ubuntu-14.04-server-amd64.iso"
  "created":["at":"20130625105211","by":10]
}
```

`GET /api/virtshell/v1/images/`
----------------------------------------------

Get all images.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/images'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "images": [
    {
      "id": "b180ef2c-e798-4a8f-b23f-aaac2fb8f7e8",
      "name": "ubuntu_server_14.04.2_amd64",
      "type": "iso",
      "os": "ubuntu",
      "permissions": "xwrxwrxwr", 
      "timezone": "America/Bogota", 
      "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu_14_04.txt",
      "download_url": "http://releases.ubuntu.com/raring/ubuntu-14.04-server-amd64.iso",
      "created":["at":"20130625105211","by":10]
    },
    {
      "id": "ca326181-bc84-4edb-bfc5-843037e7195e",
      "name": "centos:centos6",
      "type": "docker-container",
      "os": "centos", 
      "version": "centos6", 
      "permissions": "xwrxwrxwr",
      "created":["at":"20140625105211","by":12]
    },
    {
      "id": "23326181-bc84-4edb-bfc5-843037e7195e",
      "name": "ubuntu_lxc",
      "type": "lxc-container",
      "os": "ubuntu", 
      "permissions": "xwrxwrxwr",
      "download_url": "https://<host>:<port>/api/virtshell/v1/files/images/3514296#file-lxc-ubuntu",
      "created":["at":"20140625105211","by":12]
    }
  ]
}
```

`DELETE /api/virtshell/v1/images/:name`
----------------------------------------------

Delete an existing image.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/images/ubuntu_server_14.04.2_amd64'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```