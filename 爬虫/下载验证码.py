import json
import time
import requests
from lxml import etree

url = 'http://www.renren.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
}
page_text = requests.get(url=url, headers=headers).text

# 2.可以将页面数据中验证码进行解析，验证码图片下载到本地
tree = etree.HTML(page_text)
# 有时候没有验证码
codeImg_url = tree.xpath('//*[@id="verifyPic_login"]/@src')
print(codeImg_url)
# 获取了验证码图片对应的二进制数据值
# code_img = requests.get(url=codeImg_url, headers=headers).content

# with open('./code.png', 'wb') as fp:
#     fp.write(code_img)
