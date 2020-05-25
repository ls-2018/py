import os
import consul
import consul.aio

DEFAULT_CONFIG = {
    ''
}

APP_ID = 'DAX'
DB_CONFIG = dict(
    host='127.0.0.1', port=3306,
    user='root', password='1234',
    db='sanic', charset='utf8',
    minsize=1, maxsize=10,
)

ZIPKIN_SERVER = {

}
CONSUL_AGENT_HOST = '192.168.0.100'

# service
PORT = 6562
