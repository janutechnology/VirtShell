VirtShell-Command Project
=========================

VirtShell-Command is a set of shell commands which allows flexibility in the provisioning scripts.
https://pypi.python.org/pypi/virtshell_commands/

Usage
=====

vs_package
==========
For install a new package: 
	vs_package -i <<package_name>>

	for example:
	vs_package -i nginx

For remove a package: 
	vs_package -r <<package_name>>

	for example:
	vs_package -r vim

vs_service
==========
for start a service: 
	vs_service --start <<service_name>>

	for example:
	vs_service --start nginx

for stop a service:
	vs_service --stop <<service_name>>

	for example:
	vs_service --stop nginx

for restart a service:
	vs_service --restart <<service_name>>

	for example:
	vs_service --restart nginx


Additional Information
======================

Creating an egg
===============
python3 setup.py bdist_egg

Upload commands to PyPI Test
============================
In home:
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

Upload commands to PyPI Live
============================
In home:
python setup.py register -r pypi
python setup.py sdist upload -r pypi