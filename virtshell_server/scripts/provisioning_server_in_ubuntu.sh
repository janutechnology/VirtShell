echo  'export LC_ALL=C' >> ~/.bashrc
source .bashrc

echo "Creating necessaries folders..."
mkdir -p /data/db
sudo mkdir -p /var/janu/log

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 
echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list
apt-get update && apt-get -q -y install \
    nodejs\
    npm \
    git \
    mongodb-org 

mongod --dbpath .
/etc/init.d/mongod start

apt-get install -y jq curl python3-pip
pip3 install tornado
pip3 install pymongo
pip3 install gitpython
pip3 install requests

echo "Installing guest additions..."
sudo apt-get install virtualbox-guest-additions-iso
sudo apt-get install virtualbox-guest-utils
sudo shutdown -r now