import os
import socket
import json
import hashlib
CODE = {
    '1001':'上传文件，从头开始上传'
}


def file_md5(file_path):
    """
    文件进行md5加密
    :param file_path:
    :return:
    """
    obj = open(file_path,'rb')
    m = hashlib.md5()
    for line in obj:
        m.update(line)
    obj.close()
    return m.hexdigest()

def jdt(size,total_size):
    """
    显示进度条
    :return:
    """
    val = int(size / total_size * 100)
    print('\r%s%%|%s' % (val, "#" * val,), end='')

def send_file(exist_size,file_total_size):
    """
    发送文件
    :param exist_size:开始读取字节的位置
    :param file_total_size: 文件总字节大小
    :return:
    """
    f = open(file_path, 'rb')
    f.seek(exist_size)
    send_size = exist_size
    while send_size < file_total_size:
        data = f.read(1024)
        sk.sendall(data)
        send_size += len(data)
        jdt(send_size,file_total_size)
    f.close()
    print('上传成功')

def upload(file_path):
    """
    文件上传（含断点）
    :param file_path:
    :return:
    """
    file_md5_val = file_md5(file_path)
    file_name = os.path.basename(file_path)
    file_size = os.stat(file_path).st_size

    cmd_dict = {'cmd': 'upload', 'file_name': file_name, 'size': file_size, 'md5': file_md5_val}
    upload_cmd_bytes = json.dumps(cmd_dict).encode('utf-8')
    sk.sendall(upload_cmd_bytes)

    # 2. 等待服务端的响应
    response = json.loads(sk.recv(8096).decode('utf-8'))
    if response['code'] == 1001:
        send_file(0, file_size)
    else:
        # 短点续传
        exist_size = response['size']
        send_file(exist_size,file_size)

sk = socket.socket()
sk.connect(('127.0.0.1',8001))

while True:
    # upload|文件路|径
    user_input = input("请输入要执行的命令")
    # 1. 自定义协议{'cmd':'upload','file_path':'.....'}
    cmd,file_path = user_input.split('|',maxsplit=1)
    if cmd == 'upload':
        upload(file_path)
    elif cmd == 'download':
        pass




