#!/bin/bash

# this script loads the main programatic elements 
# but requires manual loading the valuestore db

# do usual apt update/upgrade before further installs

# user needs sudo privs (ideally with password auth off)
# script tested on ubuntu 18.x LTS

# handy psql access sudo -u postgres psql


sudo apt install postgresql postgresql-contrib -y
sudo systemctl enable postgresql.service 
sudo apt install python3-pip -y
sudo apt install libpq-dev -y
pip3 install psycopg2
pip3 install flask
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 5000 # flask default port
sudo ufw allow 5432 # postgres
sudo useradd -s /bin/bash -m valuestore
echo valuestore:valuestore | sudo chpasswd
sudo su - valuestore

# next manual psql loading step
# * sudo -i -u postgres
# * psql -f db.out postgres	you might have to tweek location of db.out

# if running a remote DB, remember to change connect strings in the valuemod.py scripts
# also, will need to uncomment listen_addresses = '*' in /etc/postgresql/10/main/postgresql.conf
# and add IP's/CIDR netmask under IPv4 local connections as trust in /etc/postgresql/10/main/pg_hba.conf
