#!/bin/bash

echo "Installing basic libraries..."
sudo apt-get install -y jq curl python-pip python3-pip
sudo apt-get install -y sqlite3 libsqlite3-dev
sudo apt-get install -y python-dev python3-dev
sudo pip3 install tornado
sudo pip3 install requests
sudo pip3 install psutil
sudo pip3 install docker-py
sudo pip3 install paramiko

echo "Installing docker..."
sudo apt-get autoremove -y
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo rm /etc/apt/sources.list.d/docker.list
sudo touch /etc/apt/sources.list.d/docker.list

echo "Creating directories for virtshell_provisioning_agent..."
sudo mkdir -p /var/janu/
sudo mkdir -p /var/janu/data/virtshell_provisioning_agent
sudo mkdir -p /var/janu/etc/virtshell_provisioning_agent/
sudo mkdir -p /var/janu/log/

if [ $# -gt 0 ]; then
	OS="$1"
	VER="$2"
else
	OS=$(lsb_release -si)
	VER=$(lsb_release -sr)
fi

if [ "$OS" == "Ubuntu" ] && [ "$VER" == "15.04" ]; 
then
    echo "Adding repository for Ubuntu 15.04"
	sudo su -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-wily main' >> /etc/apt/sources.list.d/docker.list"    
elif [ "$OS" == "Ubuntu" ] && [ "$VER" == "14.04" ];
then
    echo "Adding repository for Ubuntu 14.04"
	sudo su -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' >> /etc/apt/sources.list.d/docker.list"    
elif [ "$OS" == "Ubuntu" ] && [ "$VER" == "12.04" ]; 
then
    echo "Adding repository for Ubuntu 12.04"
    sudo su -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-precise main' >> /etc/apt/sources.list.d/docker.list"
else
    echo "Operating system not supported"
    exit 4
fi

sudo apt-get update
sudo apt-get purge lxc-docker
sudo apt-get install -y linux-image-extra-´$(uname -r)´
sudo apt-get install -y docker-engine

echo "Configuring docker..."
echo  'DOCKER_OPTS="-H tcp://127.0.0.1:2376 -H unix:///var/run/docker.sock --dns 8.8.8.8 --dns 8.8.4.4"' >> /etc/default/docker

echo "Starting docker..."
sudo service docker start



