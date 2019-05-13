#!/usr/bin/env python
# coding: utf-8
"""
关于主机的信息管理
"""

from django.shortcuts import render, redirect, reverse
from .host_forms import HostCreateForm
from .models import Host
from django.http import JsonResponse


def host_all(request):
    name = request.GET.get('name', '')
    hosts = Host.objects.filter(name__contains=name)
    return render(request, 'host_list.html', {'hosts': hosts, 'page_title': '主机列表', 'user': request.account})


def host_create(request, pk=0):
    obj = Host.objects.filter(pk=pk).first()
    host_obj = HostCreateForm(instance=obj)
    if request.method == "POST":
        host_obj = HostCreateForm(request.POST, instance=obj)
        if host_obj.is_valid():
            host_obj.save()
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(host_obj.errors)})
    return render(request, 'host_update.html', {'form': host_obj, 'pk': pk})


def host_delete(request, pk):
    Host.objects.filter(pk=pk).delete()
    return redirect(reverse('hostall'))
