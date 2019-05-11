# _*_coding:utf-8_*_

import sys
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(basedir)
sys.path.append(basedir)
#
from backend import main

if __name__ == '__main__':
    main.call(sys.argv[1:])
