# 第8章/cms4py_first_generation/docker/web/Dockerfile

FROM python:3-slim

# 使用清华镜像安装项目依赖项
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    asgiref Jinja2 python-socketio uvicorn websockets \
    pydal aiomysql

