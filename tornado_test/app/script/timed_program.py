#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : timed_program.py
# @Date  : 2019/9/12
# @Role  : 需要定时执行的程序

import datetime


def tail_data():
    print(datetime.datetime.now())


if __name__ == '__main__':
    tail_data()
