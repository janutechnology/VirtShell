Prerequisites
----------------------------------------------
python 3.2.3
sqlite3
tornado 4.2.1
lxc
python3-lxc

Install python 3.2.3
----------------------------------------------
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install software-properties-common libssl-dev openssl wget
wget https://www.python.org/ftp/python/3.2.3/Python-3.2.3.tgz
tar xzf Python-3.2.3.tgz
cd Python-3.2.3
sudo ./configure; make; make install
sudo ln -s /usr/local/bin/python3.2 /usr/bin/python3.2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.2 0
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.2 0
sudo update-alternatives --config python
sudo update-alternatives --config python3

Intall sqlite3
----------------------------------------------
sudo apt-get install sqlite3
sudo apt-get install libsqlite3-dev

Install tornado
----------------------------------------------
wget https://pypi.python.org/packages/source/t/tornado/tornado-4.2.1.tar.gz
tar xvzf tornado-4.2.1.tar.gz
cd tornado-4.2.1
python3.2 setup.py build
sudo python3.2 setup.py install

or

sudo pip3.2 install tornado


Install lxc
----------------------------------------------
sudo apt-get install lxc

Other packages
----------------------------------------------
sudo pip3.2 install psutil
sudo pip3.2 install websocket
sudo pip3.2 install websocket-client
