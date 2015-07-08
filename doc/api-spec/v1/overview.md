VirtShell V1
=============
A REST based virtualization service.

The sections below document the behavior of the API in detail.

Output Format
=============

The API supports only JSON output. This is the default output format, and
requesting any output format other than `application/json` via the accept
header will result in a `406 Content Not Acceptable` error.


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

* [Hosts][hosts]
 - `/api/virtsh/v1/hosts`

* [ISOS][isos] - `/api/virtsh/v1/isos`

* [Container Templates][container_templates] - `/api/virtsh/v1/container_templates`

* [Provisioners][provisioners] - `/api/virtsh/v1/provisioners`

* [Instances][intances] - `/api/virtsh/v1/intances`

* [Properties][properties] - `/api/virtsh/v1/properties`

* [Packages][packages] - `/api/virtsh/v1/packages`

* [Files][files] - `/api/virtsh/v1/files`

API Calls
=========

Below is a list of API calls don't represent directly a resource.

* [Restart host][restart_host] - `/api/virtsh/v1/restart_host`
* [Execute provisioner][execute_provisioner] - `/api/virtsh/v1/execute_provisioner`
* [Start instance][start_instance] - `/api/virtsh/v1/start_instance`
* [Stop instance][stop_instance] - `/api/virtsh/v1/stop_instance`
* [Restart instance][restart_instance] - `/api/virtsh/v1/restart_instance`
* [Destroy instance][destroy_instance] - `/api/virtsh/v1/destroy_instance`
* [Clone instance][clone_instance] - `/api/virtsh/v1/clone_instance`
* [Execute command][execute_command] - `/api/virtsh/v1/execute_command`
* [Copy file][copy_file] - `/api/virtsh/v1/copy_file`

[hosts]: hosts.md
[isos]: isos.md
[container_templates]: container_templates.md
[provisioners]: provisioners.md
[intances]: intances.md
[properties]: properties.md
[packages]: packages.md
[files]: files.md
[restart_host]: restart_host.md
[execute_provisioner]: execute_provisioner.md
[start_instance]: start_instance.md
[stop_instance]: stop_instance.md
[restart_instance]: restart_instance.md
[destroy_instance]: destroy_instance.md
[clone_instance]: clone_instance.md
[execute_command]: execute_command.md
[copy_file]: copy_file.md