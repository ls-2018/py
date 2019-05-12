#!/usr/bin/env python
# coding:utf-8

# apt-get install sysstat

import subprocess


def monitor(frist_invoke=1):
    shell_command = 'sar 1 3| grep "^Average:"'  # 依赖sysstat
    '''
[root@liushuo ~]# sar  1 3
Linux 3.10.0-514.26.2.el7.x86_64 (liushuo) 	05/12/2019 	_x86_64_	(1 CPU)

10:45:44 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
10:45:45 AM     all      0.00      0.00      0.00      0.00      0.00    100.00
10:45:46 AM     all      0.00      0.00      0.99      0.99      0.00     98.02
10:45:47 AM     all      1.00      0.00      0.00      0.00      0.00     99.00
Average:        all      0.33      0.00      0.33      0.33      0.00     99.00

    '''
    status, result = subprocess.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        # print('---res:',result)
        user, nice, system, idle = result.split()[1:]
        value_dic = {
            'user': user,
            'nice': nice,
            'system': system,
            'idle': idle,
            'status': status
        }
    return value_dic


if __name__ == '__main__':
    print(monitor())
