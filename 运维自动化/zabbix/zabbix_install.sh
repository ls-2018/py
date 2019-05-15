#!/bin/bash
##############################################################
# File Name: zabbix_install.sh
# Version: V1.0
# Author: liushuo
# Organization: www.shuoiliu.com
# Created Time : 2019-05-14 10:02:18
# Description:
##############################################################

yum install -y libevent-devel wget tar gcc gcc-c++ make net-snmp-devel libxml2-devel libcurl-devel
useradd -s /sbin/nologin zabbix
cd /usr/local/src/

wget 'https://nchc.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/4.0.3/zabbix-4.0.3.tar.gz'
tar -zxvf zabbix-4.0.3.tar.gz
cd zabbix-4.0.3
./configure --prefix=/usr/local/zabbix --enable-server --enable-agent --with-mysql=/usr/local/mysql/bin/mysql_config --with-net-snmp --with-libcurl --with-libxml2
make && make install

echo "export PATH=$PATH:/usr/local/zabbix/sbin/:/usr/local/zabbix/bin/" >> /etc/profile
source /etc/profile

# zabbix_server --version

# mysql -h 127.0.0.1 -uroot -pzabbixpwd -A
# create database zabbix character set utf8 collate utf8_bin;
# grant all privileges on zabbix.* to zabbix@'127.0.0.1' identified by 'zabbixpwd';
# flush privileges;
# set names utf8;
# use zabbix;
# source /usr/local/src/zabbix-4.0.3/database/mysql/schema.sql;
# source /usr/local/src/zabbix-4.0.3/database/mysql/data.sql;
# source /usr/local/src/zabbix-4.0.3/database/mysql/images.sql;

# 配置文件
cat > /usr/local/zabbix/etc/zabbix_server.conf << EOF

LogFile=/usr/local/zabbix/zabbix_server.log
DBHost=127.0.0.1
DBName=zabbix
DBUser=zabbix
DBPassword=用户密码
DBPort=3306
Timeout=30
#AlertScriptsPath=/usr/local/zabbix/alertscripts     # 报警脚本目录
#ExternalScripts=/usr/local/zabbix/externalscripts
LogSlowQueries=3000

EOF

chown zabbix:zabbix -R /usr/local/zabbix/
# zabbix_server
# cat /usr/local/zabbix/zabbix_server.log


# ############Zabbix Web的安装#########################
mkdir /usr/local/nginx/html/zabbix
cp -a /usr/local/src/zabbix-4.0.3/frontends/php/* /usr/local/nginx/html/zabbix/

# 根据访问首页的配置信息更改配置文件 vim /etc/local/php/etc/php.ini ,重启php-fpm
# post_max_size = 32M
# max_execution_time = 350
# max_input_time = 350 
# date.timezone = Asia/Shanghai
# always_populate_raw_post_data = -1
# systemctl restart php-fpm


# 登陆
# 默认用户名密码   Admin   zabbix
# 禁用Zabbix server 主机的监控
# 禁用guest用户
# 更改Admin密码

# 乱码
# 1、wget https://raw.githubusercontent.com/chenqing/ng-mini/master/font/msyh.tt      # 微软雅黑
# 2、mv msyh.tt /usr/local/nginx/html/zabbix/fonts/
# 3、修改/usr/local/nginx/html/zabbix/include/defines.inc.php 
	# 让DejaVuSans ----> msyh














