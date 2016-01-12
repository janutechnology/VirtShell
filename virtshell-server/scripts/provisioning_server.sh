#!/bin/bash

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
