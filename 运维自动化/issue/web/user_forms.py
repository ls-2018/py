#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
from utils.mixin import ModelForm
from .models import UserProfile
from django import forms


class UserCreateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean_email(self):
        if self.instance.pk: return self.cleaned_data['email'].strip()
        user=UserProfile.objects.filter(email=self.cleaned_data['email']).first()
        if user:
            raise forms.ValidationError(u"该邮箱已经存在")
        else:
            return self.cleaned_data['email'].strip()