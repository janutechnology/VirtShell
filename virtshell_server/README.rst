VirtShell-Server Project
========================

VirtShell-Server is a server offering a rest api to perform provisioning of 
virtual resources like virtual machines or containers.

Temporal notes:
==============
For now: python3 server.py 
rsync -azP virtshell_server/ ssh callanor@192.168.0.15:/home/callanor/virtshell_server

References:
https://github.com/tornadoweb/tornado
https://blog.openshift.com/day-25-tornado-combining-tornado-mongodb-and-angularjs-to-build-an-app/
https://github.com/paulocheque/python-rest-handler
https://github.com/shekhargulati/day25-tornado-demo-app


Configuring docker in server host
=================================
In /etc/default/docker set DOCKER_OPTS="-H tcp://127.0.0.1:2376 -H unix:///var/run/docker.sock --dns 8.8.8.8 --dns 8.8.4.4"
