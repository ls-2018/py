#!/bin/bash
yum install -y gcc gcc-c++ make tar openssl openssl-devel cmake ncurses ncurses-devel
useradd -s /sbin/nologin mysql
cd /usr/local/src
wget 'https://cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.39.tar.gz'
tar xf mysql-5.6.39.tar.gz
cd mysql-5.6.39
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/data/mysql -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_EXTRA_CHARSETS:STRING=all -DWITH_DEBUG=0 -DWITH_SSL=yes -DWITH_READLINE=1 -DENABLED_LOCAL_INFILE=1
make && make install

echo "export PATH=$PATH:/usr/local/mysql/bin/" >> /etc/profile
source /etc/profile


cp support-files/mysql.server /etc/init.d/mysqld

chmod a+x /etc/init.d/mysqld


cat > /etc/my.cnf << EOF
[mysqld]
bind-address=0.0.0.0
port=3306
datadir=/data/mysql
user=mysql
skip-name-resolve
long_query_time=2
slow_query_log_file=/data/mysql/mysql-slow.log
expire_logs_days=2
innodb-file-per-table=1
innodb_flush_log_at_trx_commit = 2
log_warnings = 1
max_allowed_packet      = 512M
connect_timeout = 60
net_read_timeout = 120

[mysqld_safe]
log-error=/data/mysql/mysqld.log
pid-file=/data/mysql/mysqld.pid
EOF


mkdir -pv /data/mysql
chown -R mysql:mysql  /usr/local/mysql /data/mysql/
yum install -y perl-Module-Install
/usr/local/mysql/scripts/mysql_install_db --basedir=/usr/local/mysql --user=mysql  --datadir=/data/mysql/

cat > /usr/lib/systemd/system/mysqld.service << EOF
[Unit]
Description=mysqld
After=network.target
[Service]
Type=forking
ExecStart=/etc/init.d/mysqld start
[Install]
WantedBy=multi-user.target
EOF


# systemctl start mysqld
# mysql -uroot -h 127.0.0.1 -A
# mysqladmin -h 127.0.0.1 -u root password 'zabbixpwd'
# mysql -h 127.0.0.1 -uroot -pzabbixpwd -A

# GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.237.%' IDENTIFIED BY 'zabbixpwd' WITH GRANT OPTION;
# flush privileges;
# mysql -h 192.168.237.49 -uroot -pzabbixpwd -A