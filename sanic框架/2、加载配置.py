from sanic import Sanic

from sanic.response import json

app = Sanic(load_env=True)
# app.config.DB_HOST=''
app.config.update({
    'DB_HOST': "localhost",
    'DB_NAME': "online",
    'DB_USER': 'root'
})
# 1、使用环境变量，前缀必须是  SANIC_
"""
例如环境变量SANIC_REQUEST_TIMEOUT在程序中自动加载并将其输入到REQUEST_TIMEOUT配置变量中，
前缀也可以自己设置，app = Sanic(load_env="MYAPP_")
"""


# 2、来自对象
class A:
    REQUEST_TIMEOUT = 121


app.config.from_object(A())

# 3、来自文件
app.config.from_pyfile('123.txt')
"""
从环境变量中指定配置文件的位置，并告诉sanic使用它来查找配置文件
app.config.from_envvar('myapp_settings')
"""
app.config.ACCESS_LOG = False  # 日志


@app.route('/')
async def test(request):
    return json({'json': "hello"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
