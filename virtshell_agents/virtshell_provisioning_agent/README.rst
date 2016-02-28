VirtShell-Provisioning-Agent Project
====================================

VirtShell-Provisioning-Agent is service that works in the hosts in order to handle the 
containers and the virtual machines.

Temporal notes:
==============
from git import Repo
Repo.clone_from("https://github.com/CALlanoR/VirtShell.git", "/root/repositories/virtshell")
https://github.com/gaelL/docker-tools/blob/master/docker_setup.py
https://github.com/lamerman/shellpy/blob/master/README.md

Temporal notes:
==============
For now: python3 server.py 
rsync -azP virtshell_provisioning_agent/ ssh root@192.168.56.102:/root/virtshell_provisioning_agent

Install
=======
copy provisioning_agent_in_ubuntu.sh in host
chmod u+x provisioning_agent_in_ubuntu.sh
./provisioning_agent_in_ubuntu