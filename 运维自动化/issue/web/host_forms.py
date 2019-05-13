#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from django import forms
from utils.mixin import ModelForm
from .models import Host
from django.http import JsonResponse


class HostCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HostCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Host
        fields = '__all__'

    def clean_name(self):
        if self.instance.pk: return self.cleaned_data['name'].strip()
        name_exist = Host.objects.filter(name=self.cleaned_data['name']).exists()
        if name_exist:
            raise forms.ValidationError("该名称已经存在")
        return self.cleaned_data['name'].strip()

    def clean_hostip(self):
        if self.instance.pk: return self.cleaned_data['hostip'].strip()
        ip_exist = Host.objects.filter(hostip=self.cleaned_data['hostip']).exists()
        if ip_exist:
            raise forms.ValidationError('该ip地址已经存在')
        return self.cleaned_data['hostip'].strip()
