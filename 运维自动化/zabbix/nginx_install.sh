yum install -y wget gcc gcc-c++ make pcre pcre-devel zlib zlib-devel openssl openssl-devel
cd /usr/local/src
yum install lrzsz -y
wget 'http://nginx.org/download/nginx-1.14.2.tar.gz'
tar -zxvf nginx-1.14.2.tar.gz
cd nginx-1.14.2
./configure --prefix=/usr/local/nginx
make && make install

echo "export PATH=$PATH:/usr/local/nginx/sbin/" >> /etc/profile

source /etc/profile

mkdir /usr/lib/systemd/system -p
cat > /usr/lib/systemd/system/nginx.service << EOF
[Unit]
Description=nginx
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/nginx/sbin/nginx
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