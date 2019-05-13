#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from utils.mixin import ModelForm
from .models import Test


class TestCreateForm(ModelForm):
    class Meta:
        model = Test
        fields = ['url', 'bingfa', 'num']
