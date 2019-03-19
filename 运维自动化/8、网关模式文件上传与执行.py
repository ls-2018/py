from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.user = "root"
env.gateway = "192.168.165.42"  # 定义堡垒机,做文件上传，执行的中转站
env.hosts = ["192.168.165.45", "192.168.165.38"]
env.password = "NFjd1234"

lpackpath = "/root/cmatrix-1.2a.tar.gz"  # 本地文件路径
rpackpath = "/tmp/test"  # 远程文件路径


@task
def put_task():
    run("mkdir -p /tmp/test")
    with settings(warn_only=True):
        result = put(lpackpath, rpackpath)
        if result.failed and not confirm("put file failed.Continue[Y/N]?"):
            abort("Aborting file put file!")


@task
def run_task():  # 执行远程命令
    with cd("/tmp/test"):
        run("tar -zxvf cmatrix-1.2a.tar.gz")
        run("ls -l")


@task
def go():  # 执行函数
    put_task()
    run_task()
#  fab -f 8、网关模式文件上传与执行.py go
#  fab -f 8、网关模式文件上传与执行.py go
