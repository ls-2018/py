#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            path = os.path.join(filepath, fi_d)
            if path.endswith('.c'):
                try:
                    with open(path, 'r', encoding='gbk') as f:
                        if r"'\x" in f.read():
                            print(path)
                except Exception:
                    with open(path, 'r', encoding='utf-8') as f:
                        if r"'\x" in f.read():
                            print(path)


# 递归遍历/root目录下所有文件
gci(r'D:\Destop\book\C')
