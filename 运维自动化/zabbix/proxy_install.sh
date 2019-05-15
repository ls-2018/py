#! /bin/bash
yum install -y tar gcc make gcc-c++ net-snmp-devel libxml2-devel libcurl-devel pcre-devel
useradd -s /sbin/nologin zabbix
cd /usr/local/src/
wget 'https://nchc.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/4.0.3/zabbix-4.0.3.tar.gz'
tar -zxvf zabbix-4.0.3.tar.gz
cd zabbix-4.0.3
./configure --prefix=/usr/local/zabbix --enable-proxy --enable-agent --with-mysql --with-net-snmp --with-libcurl --with-libxml2
make && make install
chown zabbix:zabbix /usr/local/zabbix/ -R

/usr/local/zabbix/sbin/zabbix_proxy --version