Images API Reference
==================

Image
=====
Represents an individual image on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /image/id | Gets one image by ID. |
| list | GET | /image | Retrieves the list of images. |
| create | POST | /image/id | Inserts a new image. | 
| delete | DELETE | /image/id | Deletes an existing image. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representations
========================
```json
{
  "id": "kj5436c0-dc94-13tg-82ce-9992b5d5c51b",
  "name": "ubuntu_server_14.04.2_amd64",
  "type": "iso|container",
  "os": "ubuntu", 
  "release": "trusty",
  "version": "14.04.2", 
  "variant": "server|desktop", 
  "arch": "i386|amd64", 
  "timezone": "America/Bogota", 
  "ssh_key": "-------- BEGIN PUBLIC KEY ----and a valid key here",
  "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu14-04.txt",
  "download_url": "https://<host>:<port>/api/virtshell/v1/files/images/3514296#file-lxc-ubuntu",
  "created":["at":"20130625105211","by":10],
  "details": "...."
}
```

###Examples###

`POST /api/virtsh/v1/images`
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
		 "release": "trusty",
		 "version": "14.04.2", 
		 "variant": "server", 
		 "arch": "amd64", 
		 "timezone": "America/Bogota", 
		 "key": "/home/callanor/.ssh/id_rsa.pub",
		 "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu14-04.txt"}' \
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

`GET /virtshell/api/v1/images/:id`
----------------------------------------------

Get a image.

```sh
curl -sv -H 'accept: application/json' 
     -H 'X-VirtShell-Authorization: UserId:Signature' \ 
     'http://localhost:8080/api/virtshell/v1/images?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
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
  "release": "trusty",
  "version": "14.04.2", 
  "variant": "server", 
  "arch": "amd64", 
  "timezone": "America/Bogota", 
  "preseed_url": "https://<host>:<port>/api/virtshell/v1/files/seeds/seed_ubuntu_14_04.txt",
  "created":["at":"20130625105211","by":10]
}
```

`GET /virtshell/api/v1/images/`
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
      "release": "trusty",
      "version": "14.04.2", 
      "variant": "server", 
      "arch": "amd64", 
      "timezone": "America/Bogota", 
      "preseed_file": "/home/callanor/seed_file.txt",
      "created":["at":"20130625105211","by":10]
    },
    {
      "id": "ca326181-bc84-4edb-bfc5-843037e7195e",
      "name": "centos_server",
      "type": "container",
      "os": "centos", 
      "version": "7", 
      "arch": "x86_64", 
      "download_url": "https://<host>:<port>/api/virtshell/v1/files/images/3514296#file-lxc-centos"
      "created":["at":"20140625105211","by":12]
    }
  ]
}
```

`DELETE /virtshell/api/v1/images/:id`
----------------------------------------------

Delete a existing image.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/images?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```