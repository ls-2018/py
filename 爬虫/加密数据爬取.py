from urllib import request
import requests
import base64
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
if not os.path.exists('jiandan'):
    os.mkdir('jiandan')

url = 'http://jandan.net/ooxx/page-46#comments'
page_text = requests.get(url=url, headers=headers).text

# 解析scr的密文数据
tree = etree.HTML(page_text)
src_code_list = tree.xpath('//span[@class="img-hash"]/text()')
for src_code in src_code_list:
    src = 'https:' + base64.b64decode(src_code).decode()
    img_path = 'jiandan/' + src.split('/')[-1]
    request.urlretrieve(url=src, filename=img_path)
    print(img_path + '下载完毕!!!')