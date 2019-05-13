#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from utils.mixin import ModelForm
from .models import Issue
from django import forms


class GitCreateForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['team', 'backup']


class FileCreateForm(ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='文件')

    class Meta:
        model = Issue
        fields = ['team', 'backup']
