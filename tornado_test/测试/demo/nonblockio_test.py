import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setblocking(False)

host = 'www.studyai.com'
try:
    client.connect((host, 80))  # 阻塞式的io, 建立连接过程中cpu是空闲的
except BlockingIOError as e:
    pass

while 1:
    try:
        client.send("GET {0} HTTP/1.1\r\nHost:{1}\r\nConnection:close\r\n\r\n".format('/', host).encode('utf-8'))
        print("send success")
        break
    except OSError as e:
        pass

data = b""
while 1:
    try:
        d = client.recv(1024)  # 阻塞直到有数据
    except BlockingIOError as e:
        continue

    if d:
        data += d
    else:
        break

data = data.decode('utf8')
print(data)
