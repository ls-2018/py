# 企业微信地址，个人可注册
# https://work.weixin.qq.com/
# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import requests

agentid = "xxx"
corpid = "xxx"
corpsecret = "xxx"

# get tocken
gettoken_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corpid + "&corpsecret=" + corpsecret
token_file = requests.get(url=gettoken_url)
token_data = token_file.text
token_json = json.loads(token_data)
my_token = token_json["access_token"]

# send wechart
touser = sys.argv[1]  # many user: "zhangsan|wangwu"
content = sys.argv[2]  # content
post_content = {
    "touser": touser,
    "agentid": agentid,
    "msgtype": "text",
    "text": {
        "content": content,
    }
}
json_content = json.dumps(post_content)
url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + my_token
response = requests.post(url, json_content)
print(response.text.decode("utf-8"))

if __name__ == "__main__":
    pass
    # /usr/local/zabbix/alertscripts/zabbix_wx.py "zhuang_weihong" "disk is not enough"
