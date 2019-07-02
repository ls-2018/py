"""
@Time: 2019/7/2 17:07 
@Author: liushuo
@File: test.py 
@Desc: 
@Software: PyCharm
"""
import json

data = open('index.json', 'r', encoding='utf8').read()
print(list(json.loads(data).get('terms').get('OnDemand').keys()))
