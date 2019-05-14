#!/bin/bash
##############################################################
# File Name: zabbix_agent_install.sh
# Version: V1.0
# Author: liushuo
# Organization: www.shuoiliu.com
# Created Time : 2019-05-14 10:02:18
# Description:
##############################################################
yum install -y gcc gcc-c++ make pcre-devel
useradd -s /sbin/nologin zabbix
cd /usr/local/src/
wget 'https://nchc.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/4.0.3/zabbix-4.0.3.tar.gz'
tar -zxvf zabbix-4.0.3.tar.gz
cd zabbix-4.0.3
./configure --prefix=/usr/local/zabbix --enable-agent
make && make install
chown zabbix:zabbix -R /usr/local/zabbix/

echo "export PATH=$PATH:/usr/local/zabbix/sbin/:/usr/local/zabbix/bin/" >> /etc/profile
source /etc/profile

zabbix_agent --version