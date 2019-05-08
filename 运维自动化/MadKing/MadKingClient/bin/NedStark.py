# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# D:\Destop\MadKing\MadKingClient
sys.path.append(BASE_DIR)
from core import HouseStark

if __name__ == '__main__':
    HouseStark.ArgvHandler(sys.argv)
