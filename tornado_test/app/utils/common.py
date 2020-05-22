#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 18:53
# @File    : common.py
# @Role    : 公用方法

import sys
import time
import functools


def required_login(fun):
    """
    :param fun:(self)
    :return:
    """

    # 保证被装饰的函数对象的__name__不变
    @functools.wraps(fun)
    def wrapper(request_handler_obj, *args, **kwargs):
        # 调用get_current_user方法判断用户是否登录
        if not request_handler_obj.get_current_user():
            # session = Session(request_handler_obj)
            # if not session.data:
            request_handler_obj.write(dict(errcode=400, errmsg="用户未登录"))
        else:
            fun(request_handler_obj, *args, **kwargs)

    return wrapper


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def color_print(msg, color='red', exits=False):
    '''颜色选择， 判断退出'''
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    msg = color_msg.get(color, 'red') % msg
    print(msg)
    if exits:
        time.sleep(2)
        sys.exit()
    return msg


def M2human(n):
    symbols = ('G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return '%sM' % n
