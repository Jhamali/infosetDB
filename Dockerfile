FROM ubuntu:xenial
ADD . infoset-ng
RUN apt-get update
RUN apt-get -y install sudo expect python3 python3-pip python3-dev memcached python3-setuptools
RUN useradd infoset -m 
RUN pip3 install --upgrade pip
USER infoset
RUN pip3 install -r infoset-ng/requirements.txt
CMD ["python3", "-u", "infoset-ng/infoset.py"]