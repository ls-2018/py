import getopt
import paramiko
import re
import sys


def Explain():
    '''
    定义函数，实现该脚本参数说明；
    加入选项错误，则调用改脚本。
    '''
    print('\t-V 查看版本号,更新日期')
    print('\t-i 指定单个IP地址 ')
    print('\t-G 批量指定服务器组')
    print('\t-g 列出指定服务器IP列表')
    print('\t-f 指定需要上传的文件')
    print('\t-d 目标路径下文件')
    print('\t-m 执行远程命令')


class Batch:

    def SeeServerGroup(self, group):
        self.group = group
        try:
            ipfile = open(self.group, 'r').readlines()
            for x in ipfile:
                print(x.rstrip())

        except(NameError, UnboundLocalError):
            print('服务器错误')

        else:
            print('Close')

    def RunServerGroup(self, group):
        self.group = group
        try:
            value = open(self.group, 'r').readlines()
            for x in value:
                Match = re.match('#', x)
                if Match:
                    pass
                else:
                    Host = x.rstrip()
                    Cmd = sys.argv[4]
                    Result.RunCmd(Host, Cmd)
        except Exception as e:
            print(e)

    def RunServerGroup1(self, group):
        self.group = group
        try:
            value = open(self.group, 'r').readlines()
            for x in value:
                Match = re.match('#', x)
                if Match:
                    pass
                else:
                    Host = x.rstrip()
                    localfile = sys.argv[4]
                    objectfile = sys.argvp[6]
                    UpandDownLoad(Host, localfile, objectfile)
        except Exception as e:
            print(e)

    def UpandDownLoad(self, Host, localfile, objectfile):
        self.Host = Host
        self.localfile = localfile
        self.objectfile = objectfile
        user = 'root'
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pkey_file = '/root/.ssh/id_rsa'
        key = paramiko.RSAKey.from_private_key_file(pkey_file)
        t = paramiko.Transport((self.Host, 22))
        t.connect(username=user, pkey=key)
        sftp = paramiko.SFTPClient.from_transport(t)
        if sys.argv[3] == '-f':
            sftp.put(self.localfile, self.objectfile)
            s.close()
        else:
            sftp.get(self.localfile, self.objectfile)
            s.close()

    def RunCmd(self, Host, Cmd):
        self.Host = Host
        self.Cmd = Cmd
        user = 'root'
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        KeyFile = '/root/.ssh/id_rsa'
        key = paramiko.RSAKey.from_private_key_file(KeyFile)
        ssh.connect(self.Host, 22, user, pkey=key, timeout=5)
        stdin, stdout, stderr = ssh.exec_command(self.Cmd)
        Cmd_Result = stdout.read(), stderr.read()
        if Cmd_Result:
            for line in Cmd_Result:
                print(line)
        else:
            print('No Values')
            ssh.close()


if __name__ == '__main__':
    try:
        Result = Batch()
        if sys.argv[1] == '-G' and sys.argv[3] == '-m':
            group = sys.argv[2]
            group = str(group)
            Result.RunServerGroup(group)
        elif sys.argv[1] == '-G' and sys.argv[3] == '-f' and sys.argv[5] == '-d':
            group = sys.argv[2]
            group = str(group)
            Result.RunServerGroup1(group)
        elif sys.argv[1] == '-G' and sys.argv[3] == '-d' and sys.argv[5] == '-f':
            group = sys.argv[2]
            group = str(group)
            Result.RunServerGroup1(group)
        elif sys.argv[1] == '-i' and sys.argv[3] == '-m':
            Host = sys.argv[2]
            Cmd = sys.argv[4]
            Result.RunCmd(Host, Cmd)
        elif sys.argv[1] == '-i' and sys.argv[3] == '-f' and sys.argv[5] == '-d':
            Host = sys.argv[2]
            localfile = sys.argv[4]
            objectfile = sys.argv[6]
            Result.UpandDownLoad(Host, localfile, objectfile)
        elif sys.argv[1] == '-i' and sys.argv[3] == '-d' and sys.argv[5] == '-f':
            Host = sys.argv[2]
            localfile = sys.argv[4]
            objectfile = sys.argv[6]
            Result.UpandDownLoad(Host, localfile, objectfile)
        elif sys.argv[1] == '-g':
            group = sys.argv[2]
            group = str(group)
            Result.SeeServerGroup(group)
        elif sys.argv[1] == '-V' or sys.argv[1] == '-v':
            print('Version: 0.7.29')
            print('Date:2017/04/15')
        else:
            Explain()
    except Exception as e:
        Explain()
