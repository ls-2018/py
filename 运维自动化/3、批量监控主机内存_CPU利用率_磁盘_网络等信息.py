import paramiko
import re

# 设置主机列表
host_list = ({'ip': '193.112.27.150', 'port': 22, 'username': 'root', 'password': 'godied2015@'},)
ssh = paramiko.SSHClient()
# 设置为接受不在known_hosts 列表的主机可以进行ssh连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for host in host_list:
    ssh.connect(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
    print(host['ip'])
    stdin, stdout, stderr = ssh.exec_command('cat /proc/meminfo')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)
        continue

    str_total = re.search('MemTotal:.*?\n', str_out).group()
    print(str_total)
    totalmem = re.search('\d+', str_total).group()

    str_free = re.search('MemFree:.*?\n', str_out).group()
    print(str_free)
    freemem = re.search('\d+', str_free).group()
    use = round(float(freemem) / float(totalmem), 2)
    print('当前内存使用率为：' + str(use))

    ssh.close()

