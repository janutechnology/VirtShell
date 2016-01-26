FROM ubuntu:14.04
MAINTAINER Carlos Llano <carlos_llano@hotmail.com>

################################################################################
# Enable rsyslog
################################################################################
RUN sed 's/#$ModLoad imudp/$ModLoad imudp/' -i /etc/rsyslog.conf
RUN sed 's/#$UDPServerRun 514/$UDPServerRun 514/' -i /etc/rsyslog.conf
RUN sed 's/#$ModLoad imtcp/$ModLoad imtcp/' -i /etc/rsyslog.conf
RUN sed 's/#$InputTCPServerRun 514/$InputTCPServerRun 514/' -i /etc/rsyslog.conf

EXPOSE 514/tcp 514/udp 
CMD ["/usr/sbin/rsyslogd", "-dn", "-f", "/etc/rsyslog.conf"]

################################################################################
# Install MongoDB
################################################################################
RUN echo  'export LC_ALL=C' >> ~/.bashrc
CMD ["source .bashrc"]
RUN mkdir -p /data/db

RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 \
  && echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list \
  && apt-get update && apt-get -q -y install \
    nodejs\
    npm \
    git \
    mongodb-org 

CMD ["mongod", "--dbpath", "."]
CMD ["/etc/init.d/mongod", "start"]

################################################################################
# Install requirements: pip3, tornado, pymongo and gitpython
################################################################################
RUN apt-get install -y jq curl python3-pip
RUN pip3 install tornado
RUN pip3 install pymongo
RUN pip3 install gitpython

################################################################################
# Install and configurate openssh-server
################################################################################
RUN apt-get install -y openssh-server

RUN mkdir /var/run/sshd

# Add user virtshell to the image
RUN useradd -s /bin/bash -m virtshell
RUN echo "virtshell:virtshell" | chpasswd
RUN echo "virtshell ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN echo "root:root" | chpasswd
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed "s@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g" -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

################################################################################
# Install supervisor
################################################################################
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf