#!/usr/local/bin/python3
# coding=utf8
def iso1():
    print('----')


def iso2(name='hello'):
    print('----', name)


'''
$ fab iso2
---- hello

Done.
$ fab iso2:name=asdas
---- asdas

Done.
$ fab iso2:asdas
---- asdas

Done.

'''

from fabric.api import local

'''local ，然后用它执行本地 Shell 命令并与之交互'''


def prepare_deploy():
    # local("./manage.py test my_app")
    # local("git add -p && git commit -m ' ' ")
    # local("git push")
    local('ls')


from fabric.api import local, settings, abort, run, cd, lcd
from fabric.contrib.console import confirm


def test():
    with settings(warn_only=True):  # warn_only 可以把退出换为警告,以提供更灵活的错误处理。
        code_dir = './src/django/myproject'
        with lcd(code_dir):  # 相当于运行 cd src/django/myproject
            result = local('ls', capture=True)
            print(result, '---')
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")
        '''
        confirm 函数,用于简单的 yes/no 提示。
        settings 上下文管理器提供了特定代码块特殊设置的功能。
        local 这样运行命令的操作会返回一个包含执行结果（ .failed 或 .return_code 属性）的对象。
        abort 函数用于手动停止任务的执行。
        run  和 local 类似,不过是在 远程 而非本地执行
        cd   和 lcd   类似,不过是在 远程 而非本地执行
        '''


def deploy():
    code_dir = '/home/test_for_ls'
    with settings(warn_only=True):
        with cd(code_dir):
            run("git clone https://github.com/ls-2018/book.git ")
            run('pwd')
            run('cd /home/test_for_ls/book/')
            run('pwd')
            run('touch a2.txt')
            run('git add . ')
            run('pwd',213)
            run('git commit -m "_" ')
            run("git push https://github.com/ls-2018/book.git master")
            print(123)

