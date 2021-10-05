"""
第9章/HomeSharing/app/utils/url.py
"""

import urllib.parse


def dict_to_url_params(d):
    """
    将字典转为 url 参数对字符串
    :param d:
    :return:
    """
    return '&'.join(
        '%s=%s' % (k, urllib.parse.quote(str(v))) for k, v in d.items()
    )
