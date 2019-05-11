# _*_coding:utf-8_*_

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrazyEye.settings")
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
import django

django.setup()
