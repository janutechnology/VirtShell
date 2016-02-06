VirtShell V1
=============
A REST based virtualization service.

The sections below document the behavior of the API in detail.

Output and Input Format
=======================

The API supports only JSON format, and requesting any output format other than `application/json` via the accept header will result in a `406 Content Not Acceptable` error.


Errors
------

Here is a list of error codes that may result from a query to this API on any
resource.

* `400 Bad Request`
The request could not be processed successfully because the request URI was
invalid. The response body will contain a reason for the failure. This response
indicates permanent error, and the request should not be retried without fixing
the error as indicated.

* `403 Forbidden`
The request could not be processed successfully because the requesting user
identity did not have sufficient access to process the request. This response
indicates permanent error, and the request should not be retried without fixing
the error as indicated.

* `406 Content Not Acceptable`
The requested resource is only capable of generating content not acceptable
according to the Accept headers sent in the request. This response indicates
permanent error, and the request should not be retried without specifying a
supported output format. Responses of this type do not contain a response body
due to the inability of the server to encode one.

* `404 Not Found`
The request could not be processed successfully because the request URI was
invalid. Most likely this is because the identifier was not found. This
response indicates permanent error, and the request should not be retried
without fixing the error as indicated.

* `500 Server Error`
The request could not be processed because the server encountered an unexpected
condition which prevented it from fulfilling the request.

* `501 Not Implemented`
The request could not be completed because the server either does not recognise
the request method or the resource requested does not exist.

Error responses other than `406 Content Not Acceptable` contain a JSON response
containing a brief message explaining the error in further detail. For example,
a query to `POST /api/virtsh/v1/instance` with a body of `{}` would
result in the following response:

```
HTTP/1.1 400 Bad Request
Content-Type: application/json
```
```json
{"error": "Missing input for create instance"}
 ```                                                                                                                                                    
API Resources
=============

Below is a list of resources provided by this API. Click on the heading for
more details.

* [Hosts][hosts] - `/virtshell/api/v1/hosts`

* [Images][images] - `/virtshell/api/v1/images`

* [Sections][sections] - `/virtshell/api/v1/sections`

* [Enviroments][enviroments] - `/virtshell/api/v1/enviroments`

* [Provisioners][provisioners] - `/virtshell/api/v1/provisioners`

* [Tasks][tasks] - `/virtshell/api/v1/tasks`

* [Instances][instances] - `/virtshell/api/v1/instances`

* [Properties][properties] - `/virtshell/api/v1/properties`

* [Packages][packages] - `/virtshell/api/v1/packages`

* [Files][files] - `/virtshell/api/v1/files`

* [Groups][groups] - `/virtshell/api/v1/groups`

* [Users][users] - `/virtshell/api/v1/users`

API Calls
=========

Below is a list of API calls don't represent directly a resource.

* [Start instance][apicalls] - `/api/virtsh/v1/instances/start_instance`
* [Stop instance][apicalls] - `/api/virtsh/v1/instances/stop_instance`
* [Restart instance][apicalls] - `/api/virtsh/v1/instances/restart_instance`
* [Clone instance][apicalls] - `/api/virtsh/v1/instances/clone_instance`
* [Execute command][apicalls] - `/api/virtsh/v1/instances/execute_command`
* [Copy file][apicalls] - `/api/virtsh/v1/instances/copy_file`
* [Add host to enviroment][apicalls] - `/api/virtsh/v1/enviroments/add_host`

[hosts]: hosts.md
[images]: images.md
[enviroments]: enviroments.md
[sections]: sections.md
[provisioners]: provisioners.md
[instances]: instances.md
[properties]: properties.md
[tasks]: tasks.md
[packages]: packages.md
[files]: files.md
[groups]: groups.md
[users]: users.md
[apicalls]: apicalls.md
