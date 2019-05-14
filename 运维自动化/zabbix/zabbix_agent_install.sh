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
/usr/local/zabbix/sbin/zabbix_agentd
###############################################################
# PidFile=/usr/local/zabbix/zabbix_agentd.pid
# LogFile=/usr/local/zabbix/zabbix_agentd.log
# Hostname=www_01
# Server=192.168.237.49            # zabbix server的ip地址，多个ip使用逗号分隔   被动
# ServerActive=192.168.237.49      # agent主动上传数据，如果注释这个选项，那么当前服务器的主动监控就被禁用了
# UnsafeUserParameters=1
# Include=/usr/local/zabbix/etc/zabbix_agentd.conf.d/*.conf
##############################################################