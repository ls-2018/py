# encoding=utf-8
"""
@Time: 2019/7/5 11:30 
@Author: liushuo
@File: 1.py 
@Desc: 
@Software: PyCharm
"""

import requests
import time
import json

jira_url = "http://jira.light2cloud.com:8092"


def login_jira():
    data_post = {
        'os_username': 'liushuo',
        'os_password': '@dnf2019D',
        'os_cookie': 'true',
        'os_destination': '',
        'user_role': '',
        'atl_token': '',
        'login': '登陆'
    }
    headers = {
        'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"}

    session = requests.Session()
    session.post(url=jira_url + '/secure/Dashboard.jspa', headers=headers, data=data_post)
    session.get(jira_url)

    return session


def get(session):
    url = "/jira/rest/api/2/issue/CMP-36"

    headers = {
        "Accept": "application/json",
        "Bearer": "bbbbbbbbbbbbbbbb"
    }

    response = session.get(jira_url + url, headers=headers)
    print(response.status_code)
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == '__main__':
    session = login_jira()
    get(session)
