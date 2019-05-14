# !/usr/bin/python
# -*- coding: utf-8 -*-
# curl 'https://oapi.dingtalk.com/gettoken?corpid=xxx&corpsecret=xxx'
import json, requests, sys
# 钉钉企业的地址
# https://oa.dingtalk.com/
# https://open-dev.dingtalk.com
appkey = 'dinglqpnfujc1bnvu1ip'
appsecret = 'GfuQ5HSzJ-yun1IzSecMxgQ_h4x0NloRS_K_AV-HG1WsRLGQUnoAe_mBAWyARITa'
agentid = '263761590'
touser = sys.argv[1]
content = sys.argv[2]

tockenurl = 'https://oapi.dingtalk.com/gettoken?corpid=' + appkey + "&corpsecret=" + appsecret
tockenresponse = requests.get(url=tockenurl)
tockenresult = json.loads(tockenresponse.text)
tocken = tockenresult['access_token']
sendurl = 'https://oapi.dingtalk.com/message/send?access_token=' + tocken
headers = {
    'Content-Type': 'application/json'
}
main_content = {
    "touser": touser,
    "toparty": "",
    "agentid": agentid,
    "msgtype": "text",
    "text": {
        "content": content
    }
}
main_content = json.dumps(main_content)
req = requests.get(url=sendurl, headers=headers)
response = requests.post(url=req, data=main_content)
print(response.text)
if __name__ == '__main__':
    pass
# python zabbix_senddd.py manager1572 'zabbix告警'
