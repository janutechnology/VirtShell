VirtShell-Server Project
========================

VirtShell-Server is a server offering a rest api to perform provisioning of 
virtual resources like virtual machines or containers.

Temporal notes:
==============
For now: python3 server.py 
rsync -azP virtshell_server/ ssh root@172.17.0.2:/root/virtshell_server

References:
https://github.com/tornadoweb/tornado
https://blog.openshift.com/day-25-tornado-combining-tornado-mongodb-and-angularjs-to-build-an-app/
https://github.com/paulocheque/python-rest-handler
https://github.com/shekhargulati/day25-tornado-demo-app