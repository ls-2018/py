# _*_coding:utf-8_*_
import subprocess


def monitor(frist_invoke=1):
    value_dic = {}
    shell_command = 'w'
    result = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()
    '''
10:32:10 up 109 days, 16:26,  1 user,  load average: 0.00, 0.03, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     pts/0    121.28.69.79     10:29    2.00s  0.02s  0.00s w
    '''
    value_dic = {
        'uptime': result,

        'status': 0
    }
    return value_dic


if __name__ == '__main__':
    print(monitor())
