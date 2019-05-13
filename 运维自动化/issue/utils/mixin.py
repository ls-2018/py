# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
from web import models
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin as DjangoLoginRequiredMixin


class ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ModelForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info.startswith('/admin/'):
            return
        if request.path_info in [reverse('login')]:
            return
            # 获取用户ID
        pk = request.session.get('user_id')
        user = models.UserProfile.objects.filter(pk=pk).first()
        if user:
            request.account = user
        else:
            return redirect(reverse('login'))


from email.mime.text import MIMEText
import smtplib


def send_mail(to_list, sub, content):
    mail_host = "smtp.51credit.com"
    mail_user = 'alert2@51credit.com'
    mail_pass = 'alert2'
    mail_postfix = 'pop.51credit.com'
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(str(content), _charset="utf-8")
    msg["Subject"] = sub
    msg["From"] = me
    msg["To"] = to_list
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.login(mail_user, mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()


def RequestDef(fuc):
    def waper():
        pass

    return waper
