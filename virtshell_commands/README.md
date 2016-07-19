VirtShell-Command Project
=========================

VirtShell-Command is a set of shell commands which allows flexibility in the provisioning scripts.
https://pypi.python.org/pypi/virtshell_commands/

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