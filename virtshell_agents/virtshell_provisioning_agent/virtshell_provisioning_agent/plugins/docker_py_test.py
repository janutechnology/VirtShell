import time
from io import BytesIO
from docker import Client
client = Client(version='1.20', base_url='tcp://127.0.0.1:2376')

distribution = "ubuntu:15.04"

dockerfile = '''
FROM ''' + distribution + '''
MAINTAINER Carlos Llano <carlos_llano@hotmail.com>
RUN sed 's/#$ModLoad imudp/$ModLoad imudp/' -i /etc/rsyslog.conf
RUN sed 's/#$UDPServerRun 514/$UDPServerRun 514/' -i /etc/rsyslog.conf
RUN sed 's/#$ModLoad imtcp/$ModLoad imtcp/' -i /etc/rsyslog.conf
RUN sed 's/#$InputTCPServerRun 514/$InputTCPServerRun 514/' -i /etc/rsyslog.conf
EXPOSE 514/tcp 514/udp 
CMD ["/usr/sbin/rsyslogd", "-dn", "-f", "/etc/rsyslog.conf"]
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN useradd -s /bin/bash -m virtshell
RUN echo "virtshell:virtshell" | chpasswd
RUN echo "virtshell ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo "root:root" | chpasswd
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/" /etc/ssh/sshd_config
RUN sed "s@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g" -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
'''
dockerfile_binary = BytesIO(dockerfile.encode('utf-8'))
response = [line for line in client.build(fileobj=dockerfile_binary,
                                          rm=True,
                                          tag='ubuntu/15.04')]
print (response)
print ("virtshell_containers_image created...")
print(response)


container = client.create_container(image='ubuntu:15.04')
container_id = container['Id']

print ("container created...")

client.start(container_id)
link_path = client.inspect_container(container_id)
print(link_path['NetworkSettings']['IPAddress'])

