Files API Reference
===================

Files
=====
Represents an individual file on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /files/:name | Gets one file by name. |
| get | GET | /files/ | Gets all files. |
| create | POST | /files/ | Upload a new file. | 
| delete | DELETE | /files/:name | Deletes an existing file. |
| update | PUT | /files/:name | Updates an existing file. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "file_name.extension",
  "directory_path" : "directory_path",
  "location": "path in the server",
  "uri": "https://<host>:<port>/api/virtshell/v1/files/directory_path/file.txt",
  "permissions": string,
  "created":["at":"timestamp", "by":user_id]
}
```

###Examples###

`POST /api/virtshell/v1/files`
--------------------------------------------

Uploading files. To upload a file to VirtShell, send a POST request to the files URL, postfixed with the name of the file. The request must contain the Content-Type header multipart/form-data and the request must indicate a specific name for the file you want to upload and the folder name where the file will be saved on the server. Here's a simple example that'll create a file named seed_file_ubuntu-14_04.txt containing a string on the folder ubuntu_seeds:

```sh
curl -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -H "Content-Type: multipart/form-data" \
  -F "file_data=@/path/to/file/seed_file.txt;filename=seed_file_ubuntu-14_04.txt" \
  -F "folder_name=ubuntu_seeds" \
  -F "permissions=xwrxwrxwr" \
  http://<host>:<port>/api/virtshell/v1/files/
```

Response:

```
HTTP/1.1 201 Created
Content-Type: application/json
```
```json
{ 
  "create": "success",
  "uri": "http://<host>:<port>/api/virtshell/v1/files/seed_file_ubuntu-14_04.txt"
}
```

`GET /api/virtshell/v1/files/:name
----------------------------------------------

To download a file:

First, retrieve the appropriate download URL (URI) provided in the file's metadata.
Then, retrieve the actual file content (or link) using the download URL.


```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://<host>:<port>/api/virtshell/v1/static/files/dockerfile_ubuntu_server_14.04.2'
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "file_name.extension",
  "uri": "http://<host>:<port>/api/virtshell/v1/files/seed_file_ubuntu-14_04.txt",
  "created":["at":"timestamp", "by":user_id] 
}
```

`PUT /api/virtshell/v1/files/:name`
----------------------------------------------

Update an existing file.

```sh
curl -sv -X PUT \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -H "Content-Type: multipart/form-data" \
  -F "permissions=xwrxwrxwr" \
  -F "file_data=@/path/to/file/seed_file.txt;filename=seed_file_ubuntu-14_04_v2.txt" \
   'http://localhost:8080/api/virtshell/v1/files/http://<host>:<port>/api/virtshell/v1/files/ubuntu_seeds/seed_file_ubuntu-14_04.txt'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "update": "success" }
```

`DELETE /api/virtshell/v1/files/:name`
----------------------------------------------

Delete an existing file.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/files/http://<host>:<port>/api/virtshell/v1/files/seed_file_ubuntu-14_04.txt'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```