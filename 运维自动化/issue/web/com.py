#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import render, redirect, reverse
from .comm_forms import CommandCreateForm
from .models import Command
from django.http import JsonResponse
from utils.ansible2.runner import AdHocRunner, CommandRunner, PlayBookRunner
from utils.ansible2.inventory import Inventory


def command_all(request):
    name = request.GET.get('name', '')
    coms = Command.objects.filter(name__contains=name)
    return render(request, 'command_list.html', {"page_title": "命令列表", "coms": coms, 'user': request.account})


def command_create(request):
    com_obj = CommandCreateForm()
    if request.method == "POST":
        com_obj = CommandCreateForm(request.POST)
        if com_obj.is_valid():
            hosts = com_obj.cleaned_data['host']

            host_data = [{"hostname": i, "ip": i, "port": 22, "username": "root"} for i in hosts.hostip]
            inventory = Inventory(host_data)
            runner = CommandRunner(inventory)

            res = runner.execute('pwd', 'all')
            print(res.results_command)
            print(res.results_raw)
            print(res.results_command['10.211.55.13']['stdout'])

            com_obj.save()
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(com_obj.errors)})
    return render(request, 'command_create.html', {'form': com_obj})


def command_delete(request, pk):
    Command.objects.filter(pk=pk).delete()
    return redirect(reverse('comall'))
