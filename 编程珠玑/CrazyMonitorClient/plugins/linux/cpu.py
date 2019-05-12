# _*_coding:utf-8_*_
import subprocess


def monitor(frist_invoke=1):
    value_dic = {}
    shell_command = 'top'
    result = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
    ''' 
top - 10:29:29 up 109 days, 16:23,  1 user,  load average: 0.03, 0.05, 0.05
Tasks:  82 total,   1 running,  80 sleeping,   0 stopped,   1 zombie
%Cpu(s):  0.7 us,  0.3 sy,  0.0 ni, 98.0 id,  1.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1883844 total,    95560 free,   463828 used,  1324456 buff/cache
KiB Swap:  4095996 total,  3962740 free,   133256 used.  1215164 avail Mem 
    '''
    # user,nice,system,iowait,steal,idle = result.split()[2:]
    value_dic = {
        'uptime': result,

        'status': 0
    }
    return value_dic


if __name__ == '__main__':
    print(monitor())
