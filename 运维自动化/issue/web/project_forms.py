#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from django import forms
from utils.mixin import ModelForm
from .models import Team, Host, UserProfile


class ProjectCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.fields['host'].choices = [(h.pk, h.hostip) for h in Host.objects.filter(type="1")]
        self.fields['nginxhost'].choices = [(h.pk, h.hostip) for h in Host.objects.filter(type="0")]
        self.fields['user_id'].choices = [(u.pk, u.name) for u in UserProfile.objects.filter(role="0")]
        self.fields['test_user'].choices = [(u.pk, u.name) for u in UserProfile.objects.filter(role="1")]

    class Meta:
        model = Team
        fields = '__all__'

    def clean_name(self):
        if self.instance.pk: return self.cleaned_data['name'].strip()
        name_exist = Team.objects.filter(name=self.cleaned_data['name']).exists()
        if name_exist:
            raise forms.ValidationError("该名称已经存在")
        return self.cleaned_data['name'].strip()
