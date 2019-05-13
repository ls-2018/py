#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from utils.mixin import ModelForm
from .models import Command


class CommandCreateForm(ModelForm):
    class Meta:
        model = Command
        fields = ['name', 'team', 'command']
