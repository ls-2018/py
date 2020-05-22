import json

import requests

web_url = "http://127.0.0.1:9001"


def test_sms():
    url = f"{web_url}/code/"
    data = {
        "mobile": "15002959016"
    }
    res = requests.post(url, json=data)

    print(res.text)


def test_register():
    url = f"{web_url}/register/"
    data = {
        "mobile": "15002959016",
        "code": '3266',
        "password": 'qaz@wsx.123'
    }
    res = requests.post(url, json=data)

    print(res.text)


if __name__ == "__main__":
    # test_sms()
    test_register()