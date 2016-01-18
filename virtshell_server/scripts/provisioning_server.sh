#!/bin/bash

echo "Installing docker..."
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo rm /etc/apt/sources.list.d/docker.list
sudo touch /etc/apt/sources.list.d/docker.list
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >> /etc/apt/sources.list.d/docker.list
sudo apt-get update
apt-get purge lxc-docker
sudo apt-get install linux-image-extra-´$(uname -r)´
sudo apt-get install docker-engine
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
