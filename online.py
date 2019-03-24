#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from fabric.api import *
from fabric import context_managers


def remote_task():
    with cd("/usr/local/myblog"):
        run('pwd')
        import time
        time.sleep(3)
        run("rm -rf ./*")
        # run('git clone https://github.com/ls-2018/online_deploy.git')
        # with context_managers.settings(hide('warnings', 'running', 'stdout', 'stderr'), warn_only=True):
        with context_managers.settings(warn_only=True):
            run('ps aux|grep uwsgi')
            run('ps aux|grep python*')
            run('pkill -9 uwsgi')
            run('pkill -9 python*')
            print('已清除残存进程')

        with cd("./online_deploy"):
            run('python3 manage.py collectstatic')
            run('pwd')
            run('setsid uwsgi --ini uwsgi_myblog.ini')
            run('pwd')
            run('setsid python3  ./log_handler/finally_log.py &')


#  fab -f 6、查看本地与远程主机信息.py remote_task
# ssh-keygen -t rsa -b 2048 -C "1214972346@qq.com"


"""
pip3 uninstall cryptography==2.5
pip3 install cryptography==2.4.2
"""
