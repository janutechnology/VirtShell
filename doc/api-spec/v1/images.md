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
| update | PUT | /image/id | Updates an existing image. |

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
  "preseed_file": "/home/callanor/seed_file.txt",
  "url": "https://gist.github.com/hagix9/3514296#file-lxc-centos",
  "path_image": "/home/cllano/templates/my-lxc-centos",  
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
		 "preseed_file": "/home/callanor/seed_file.txt"}' \
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

`GET /virtshell/api/v1/images/`
----------------------------------------------

`POST /virtshell/api/v1/images/`
----------------------------------------------

`PUT /virtshell/api/v1/images/:id`
----------------------------------------------

`DELETE /virtshell/api/v1/images/:id`
----------------------------------------------