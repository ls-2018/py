# coding: utf-8

from utils.ansible2.runner import AdHocRunner, CommandRunner, PlayBookRunner
from utils.ansible2.inventory import Inventory


def TestAdHocRunner():
    """
     以yml的形式 执行多个命令
    :return:
    """
    host_data = [
        {
            "hostname": "10.211.55.13",
            "ip": "10.211.55.13",
            "username": "root",
        },
    ]
    inventory = Inventory(host_data)
    runner = AdHocRunner(inventory)
    # dest = "/opt/mysql/world.sh"

    tasks = [
        {"action": {"module": "shell", "args": "whoami"}, "name": "run_whoami"},
        {"action": {"module": "replace", "args": 'path=/tmp/a.txt regexp="^(192.168.1.1.*)" replace="#\\1"'},
         "name": "down nginx"}
        # {"action": {"module": "shell", "args": "free -m | awk 'NR\=\=2{printf \"%.2f\", $3*100/$2 }'"}, "name": "get_mem_usage"},
        # {"action": {"module": "shell", "args": "df -h | awk '$NF\=\=\"/\"{printf \"%s\", $5}'"}, "name": "get_disk_usage"},
        # {"action": {"module": "copy", "args": "src=/home/python/Desktop/3358.cnf dest=/opt/mysql/my3358.cnf mode=0777"}, "name": "send_file"},
        # {"action": {"module": "copy", "args": "src=/home/python/Desktop/deploy.sh dest=/opt/mysql/deploy.sh mode=0777"}, "name": "send_file"},
        # {"action": {"module": "command", "args": "sh /opt/mysql/hello.sh"}, "name": "execute_file"},
        # {"action": {"module": "shell", "args": "sudo sh /opt/mysql/deploy.sh"}, "name": "execute_file"},
        # {"action": {"module": "lineinfile", "args": "dest=/opt/mysql/hello.sh line=hello1 regexp=echo state=present"}, "name": "modify_file"},
        # {"action": {"module": "lineinfile", "args": "dest=/opt/mysql/world.sh line="" regexp=echo state=present"}, "name": "modify_file"},
        # {"action": {"module": "lineinfile", "args": "dest=%s line=sun regexp=echo state=present" % dest}, "name": "modify_file"},
        # {"action": {"module": "shell", "args": "lineinfile dest=/opt/mysql/hello.sh regexp=hello insertafter=#echo line=hello world"}, "name": "modify_file"},

        # {"action": {"module": "shell", "args": "grep 'cpu ' /proc/stat | awk '{usage\=($2+$4)*100/($2+$4+$5)} END {print usage}'"}, "name": "get_cpu_usage"},
    ]
    ret = runner.run(tasks)
    print(ret.results_summary)
    print(ret.results_raw)


def TestCommandRunner():
    """
    执行单个命令，返回结果
    :return:
    """

    host_data = [
        {
            "hostname": "10.211.55.13",
            "ip": "10.211.55.13",
            "port": 22,
            "username": "root",
            # "private_key": "/home/python/.ssh/id_rsa_1",
        },
    ]
    inventory = Inventory(host_data)
    runner = CommandRunner(inventory)

    res = runner.execute('pwd', 'all')
    print(res.results_command)
    print(res.results_raw)
    print(res.results_command['10.211.55.13']['stdout'])


def TestPlayBookRunner():
    """
    执行playbook
    :return:
    """
    host_data = [
        {
            "hostname": "10.211.55.13",
            # "ip": "10.211.55.13",
            "port": 22,
            "username": "root",
            # "list_hosts":"all"
            # "private_key": "/home/python/.ssh/id_rsa_1",
        },
    ]
    inventory = Inventory(host_data)
    opstions = {
        "playbook_path": "/Users/derekwang/test/a.yml"
    }
    runner = PlayBookRunner(inventory, options=opstions, playbook_path="/Users/derekwang/test/a.yml").run()
    print(runner)


if __name__ == "__main__":
    TestAdHocRunner()
    # TestCommandRunner()
    # TestPlayBookRunner()
