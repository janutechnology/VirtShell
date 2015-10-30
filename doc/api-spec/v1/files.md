Files API Reference
===================

Files
=====
Represents an individual file on VirtShell.

| Method | HTTP request | Description |
| --- | --- | ---- |
| get | GET | /files/id | Gets one file by ID. |
| create | POST | /files/ | Upload a new file. | 
| delete | DELETE | /files/id | Deletes an existing file. |

Note:
URIs relative to https://www.yourhostname.com/api/virtshell/v1, unless otherwise noted.

Resource representation
=======================
```json
{
  "uuid": "ab8076c0-db91-11e2-82ce-0002a5d5c51b",
  "name": "file_name.extension",
  "folder_name" : "folder_name",
  "download_url": "https://<host>:<port>/api/virtshell/v1/files/folder_name/file.txt",
  "created":["at":"timestamp", "by":user_id]
}
```

###Examples###

`POST /virtshell/api/v1/files`
--------------------------------------------

Uploading files. To upload a file to VirtShell, send a POST request to the files URL, postfixed with the name of the file. The request must contain the Content-Type header multipart/form-data and the request must indicate a specific name for the file you want to upload and the folder name where the file will be saved on the server. Here's a simple example that'll create a file named seed_file_ubuntu-14_04.txt containing a string on the folder ubuntu_seeds:

```sh
curl -X POST \
  -H 'accept: application/json' \
  -H 'X-VirtShell-Authorization: UserId:Signature' \
  -H "Content-Type: multipart/form-data" \
  -F "file_data=@/path/to/file/seed_file.txt;filename=seed_file_ubuntu-14_04.txt" \
  -F "folder_name=ubuntu_seeds" \
  http://<host>:<port>/api/virtshell/v1/files/
```

Response:

```
HTTP/1.1 201 Created
Content-Type: application/json
```
```json
{ "create": "success",
  "location": "http://<host>:<port>/api/virtshell/v1/files/ubuntu_seeds/seed_file_ubuntu-14_04.txt" }
```

`GET /virtshell/api/v1/files/:id
----------------------------------------------

To download a file:

First, retrieve the appropriate download URL provided in the file's metadata.
Then, retrieve the actual file content (or link) using the download URL.


```sh
curl -sv -H 'accept: application/json' 
		 -H 'X-VirtShell-Authorization: UserId:Signature' \ 
		 'http://<host>:<port>/api/virtshell/v1/files/?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
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
  "folder_name" : "folder_name",
  "download_url": "http://<host>:<port>/api/virtshell/v1/files/ubuntu_seeds/seed_file_ubuntu-14_04.txt",
  "created":["at":"timestamp", "by":user_id] 
}
```

`DELETE /virtshell/api/v1/files/:id`
----------------------------------------------
Delete a existing file.

```sh
curl -sv -X DELETE \
   -H 'accept: application/json' \
   -H 'X-VirtShell-Authorization: UserId:Signature' \
   'http://<host>:<port>/api/virtshell/v1/files?id=ab8076c0-db91-11e2-82ce-0002a5d5c51b'
```

Response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{ "delete": "success" }
```