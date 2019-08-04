import requests
import time

f1 = open("1234.mp4", 'ab+')
for i in range(0, 1069):
    url = 'https://youku.pmkiki.com/20190727/8HMwqKYP/1000kb/hls/qkOQOTdk2588%03d.ts' % i
    path = "./movie/qkOQOTdk2588%03d.ts" % i
    print(path)
    response = requests.get(url)
    time.sleep(1)
    with open(path, 'wb') as f:
        f.write(response.content)
    f1.write(response.content)
f1.close()
