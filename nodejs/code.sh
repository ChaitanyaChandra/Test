#!/bin/bash
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install nodejs -y 

yum install git -y 
git clone https://github.com/ChaitanyaChandra/spec.git
cd spec/
npm  install
node index.js > node.logs 2>&1 &
ps -ef | grep "index.js" > run.log


# cloud watch logs

# install wget to download
sudo yum install wget -y 

# download rpm using wget
wget https://s3.amazonaws.com/amazoncloudwatch-agent/centos/amd64/latest/amazon-cloudwatch-agent.rpm

# install downloaded rpm
sudo rpm -U ./amazon-cloudwatch-agent.rpm

# create a dir to avoid errors
sudo mkdir -p /usr/share/collectd/
sudo touch /usr/share/collectd/types.db

# download config file 
wget https://raw.githubusercontent.com/ChaitanyaChandra/spec/master/config.json

# run agent 
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:config.json