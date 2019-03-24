from fabric.api import *

env.user = "root"
env.hosts = ["192.168.165.45", "192.168.165.38"]
env.password = "NFjd1234"

@runs_once
def input_raw():
        return prompt("Pleace input dir_name:",default="/home")

def worktask(dirname):
        run("ls -l " + dirname)

@task
def go():
        getdirname = input_raw()
        worktask(getdirname)

#  fab -f 7、动态获取远程主机目录列表.py go
#  fab -f 7、动态获取远程主机目录列表.py local_task
