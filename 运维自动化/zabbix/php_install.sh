#!/bin/bash
##############################################################
# File Name: 1.sh
# Version: V1.0
# Author: liushuo
# Organization: www.shuoiliu.com
# Created Time : 2019-05-14 09:34:20
# Description:
##############################################################
yum -y install epel-release gcc gcc-c++ make pcre pcre-devel zlib zlib-devel openssl openssl-devel libxml2 libxml2-devel libcurl libcurl-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel openldap openldap-devel libmcrypt libmcrypt-devel
cd /usr/local/src

wget 'http://hk1.php.net/distributions/php-5.6.40.tar.gz'
tar -zxf php-5.6.40.tar.gz
cd php-5.6.40


./configure --prefix=/usr/local/php --with-config-file-path=/usr/local/php/etc --enable-ctype --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-libxml-dir=/usr --enable-xml --disable-rpath --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --with-curl --enable-mbregex --enable-mbstring --with-mcrypt --with-gd --enable-gd-native-ttf --with-openssl --with-mhash --enable-pcntl --enable-sockets --with-ldap-sasl --with-xmlrpc --enable-zip --enable-soap --with-gettext --enable-fpm
make && make install

echo "export PATH=$PATH:/usr/local/php/sbin/:/usr/local/php/bin/" >> /etc/profile
source /etc/profile

cp php.ini-production /usr/local/php/etc/php.ini
mv /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf

mkdir /usr/lib/systemd/system -p
cat > /usr/lib/systemd/system/php-fpm.service << EOF
[Unit]
Description=php-fpm
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/php/sbin/php-fpm
[Install]
WantedBy=multi-user.target
EOF

# location / {
#      root   html;
#      index  index.html index.htm index.php;
# }
# location ~ \.php$ {
#       root           html;
#       fastcgi_pass   127.0.0.1:9000;
#       fastcgi_index  index.php;
#       fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
#       include        fastcgi_params;
#   }
#   
# systemctl start php-fpm
