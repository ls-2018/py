# 企业内部开发
# https://work.weixin.qq.com/wework_admin/frame
# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import requests

agentid = "1000002"
corpid = "ww3144e40350ed3124"  # 企业微信的CorpID
corpsecret = ""

# get tocken
# https://work.weixin.qq.com/api/doc#90000/90003/90487
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
print(response.text)

if __name__ == "__main__":
    pass
    # python zabbix_sendwx.py "LiuShuo" "disk is not enough"
