# 阻塞式 IO
import requests

html = requests.get('http://studyai.com').text
# 1. 三次握手建立tcp连接
# 2. 等待服务器响应
# requests ==》 urllib3  ===> socket
# print(html)

# 如何通过socket直接获取html页面数据？
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'www.studyai.com'
client.connect((host, 80))  # 阻塞式的io, 建立连接过程中cpu是空闲的
client.send("GET {0} HTTP/1.1\r\nHost:{1}\r\nConnection:close\r\n\r\n".format('/', host).encode('utf-8'))

data = b""
while 1:
    d = client.recv(1024)  # 阻塞直到有数据
    if d:
        data += d
    else:
        break

data = data.decode('utf8')
print(data)
