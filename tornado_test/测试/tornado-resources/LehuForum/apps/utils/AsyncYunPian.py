import json

import requests
from tornado import httpclient


class AsyncYunPian:
    def __init__(self, api_key):
        self.api_key = api_key

    async def send_single_sms(self, code, mobile):
        http_client = httpclient.AsyncHTTPClient()
        # 发送单条短信

        url = "https://sms.yunpian.com/v2/sms/single_send.json"
        #         # text = "【慕学生鲜】您的验证码是{}。如非本人操作，请忽略本短信".format(code)
        #         # postRequest = httpclient.HTTPRequest(url=url, method='POST', body=urlencode({
        #         #     "apikey": self.api_key,
        #         #     "mobile": mobile,
        #         #     "text": "text"
        #         # }))
        #         # res = await http_client.fetch(postRequest)
        res = requests.post(url, data={
            "apikey": 'd715a3bbc04533805573da0ab886f4a2',
            "mobile": '15733101139',
            "text": "(123)"
        }
                            )
        print(res.content.decode('utf8'))
        return json.loads(res.text)


if __name__ == "__main__":
    from tornado import ioloop

    loop = ioloop.IOLoop.current()
    yunpian = AsyncYunPian("d715a3bbc04533805573da0ab886f4a2")
    # run_sync方法可以在运行完某个协程之后停止事件循环
    from functools import partial

    new_func = partial(yunpian.send_single_sms, '1234', '15733101139')
    loop.run_sync(new_func)
    ioloop.IOLoop.current().start()
# WARNING:tornado.general:SSL Error on 7 ('118.178.213.2', 443): [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)
# Traceback (most recent call last):
# /Applications/Python\ 3.7/Install\ Certificates.command
