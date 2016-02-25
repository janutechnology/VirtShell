echo  'export LC_ALL=C' >> ~/.bashrc
source .bashrc
mkdir -p /data/db

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
