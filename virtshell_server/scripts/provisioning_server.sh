#!/bin/bash

echo "Installing docker..."
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo rm /etc/apt/sources.list.d/docker.list
sudo touch /etc/apt/sources.list.d/docker.list

OS=$(lsb_release -si)
VER=$(lsb_release -sr)
if [ "$OS" == "Ubuntu" ] && [ "$VER" == "15.04" ]; 
then
    echo "Adding repository for Ubuntu 15.04"
    echo "deb https://apt.dockerproject.org/repo ubuntu-wily main" >> /etc/apt/sources.list.d/docker.list
elif [ "$OS" == "Ubuntu" ] && [ "$VER" == "14.04" ];
then
    echo "Adding repository for Ubuntu 14.04"
    echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >> /etc/apt/sources.list.d/docker.list
elif [ "$OS" == "Ubuntu" ] && [ "$VER" == "12.04" ]; 
then
    echo "Adding repository for Ubuntu 12.04"
    echo "deb https://apt.dockerproject.org/repo ubuntu-precise main" >> /etc/apt/sources.list.d/docker.list
else
    echo "Operating system not supported"
    exit 4
fi

sudo apt-get update
sudo apt-get purge lxc-docker
sudo apt-get install -y linux-image-extra-´$(uname -r)´
sudo apt-get install -y docker-engine
sudo service docker start

echo "Creating virtshell image..."
sudo docker build -t virtshell_server_image .

echo "Creating virtshell server container..."
sudo docker run -d -P --name=virtshell_server virtshell_server_image

echo "Checking ssh port..."
sudo docker port virtshell_server 22

echo "Obtaining container id..."
ID="$(sudo docker inspect --format '{{ .Id }}' virtshell_server)"
echo "Container id: $ID"

echo "Obtaining container ip address..."
IP="$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' $ID)"
echo "IP address: $IP"
echo "login with: ssh root@$IP, password is root, please change it."
