#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fabric.api import *

env.user = "root"
env.hosts = ["192.168.165.45", "192.168.165.38"]
env.password = "NFjd1234"


@runs_once  # 查看本地系统信息，当有多台主机时只运行一次
def local_task():  # 本地任务函数
    local("uname -a")
    local("df -h")


def remote_task():
    with cd("/home"):  # with的作用是让后面的表达式语句集成当前状态，效果相对于"cd /home && ls -l"
        run("ls -l")

#  fab -f 6、查看本地与远程主机信息.py local_task
#  fab -f 6、查看本地与远程主机信息.py remote_task
