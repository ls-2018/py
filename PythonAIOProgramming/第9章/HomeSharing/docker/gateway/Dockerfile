# 第8章/cms4py_first_generation/docker/gateway/Dockerfile

FROM php:apache

# 启用重写模块
RUN a2enmod rewrite
# 启用 http 代理模块
RUN a2enmod proxy_http
# 启用 FastCGI 代理模块
RUN a2enmod proxy_fcgi
# 启用 WebSocket 代理模块
RUN a2enmod proxy_wstunnel


# 用自定义的配置文件替换 Apache 配置文件
COPY 000-default.conf /etc/apache2/sites-enabled