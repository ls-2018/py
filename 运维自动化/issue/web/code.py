#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, reverse, redirect,HttpResponse
from .code_forms import *
from django.http import JsonResponse
from web.models import Issue, Host_Issue
import random
from utils.ansible2.runner import AdHocRunner
from utils.ansible2.inventory import Inventory
import time
import os
from django.views.decorators.csrf import csrf_exempt
import subprocess
from django.db.models import Q



def update_all(request):
    if request.path_info == reverse('updateall'):
        all = Issue.objects.filter(Q(user=request.account)|Q(team__test_user=request.account))
        page_title='更新记录'
        html='update_list.html'
    else:
        all = Issue.objects.filter(Q(user=request.account)| Q(team__test_user=request.account),status='6')
        page_title='回滚记录'
        html='rollback_list.html'
    return render(request, html, {"page_title":page_title, "issues": all,'user':request.account})


def git_create(request):
    git_obj = GitCreateForm()
    if request.method == "POST":
        git_obj = GitCreateForm(request.POST)
        if git_obj.is_valid():
            t = int(time.time())
            git_obj.instance.src_path = t
            git_obj.instance.user = request.account
            git_obj.instance.type = '1'
            subprocess.getoutput('cd {} && git pull'.format(os.path.join('/upload',git_obj.cleaned_data['team'].name)))
            issue = git_obj.save()
            hosts = git_obj.cleaned_data['team'].host.all()
            for host in hosts:
                Host_Issue.objects.create(**git_obj.cleaned_data, host=host, issue=issue, user=request.account,
                                          type="1")
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(git_obj.errors)})
    return render(request, 'git_create.html', {'form': git_obj})


def handle_uploaded_file(f,t):
    print(f,t)
    with open(os.path.join('/upload',os.path.join(t, f.name)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def file_create(request):
    file_obj = FileCreateForm()
    if request.method == "POST":
        file_obj = FileCreateForm(request.POST, request.FILES)
        if file_obj.is_valid():
            t = int(time.time())
            file_obj.instance.src_path = t
            file_obj.instance.user = request.account
            file_obj.instance.type = '0'
            # for file in request.FILES.getlist('file_field'):
            #     handle_uploaded_file(file,t)
            issue = file_obj.save()
            hosts = file_obj.cleaned_data['team'].host.all()
            file_obj.cleaned_data.pop('file_field')
            for host in hosts:
                Host_Issue.objects.create(**file_obj.cleaned_data, host=host, issue=issue, user=request.account,
                                          type="0")
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(file_obj.errors)})
    return render(request, 'file_create.html', {'form': file_obj})


def code_detail(request, pk):
    obj = Issue.objects.filter(pk=pk).first()
    return render(request, 'code_detail.html', {'code': obj})


def update(request, pk):
    """
    随机挑选一个机器进行发布，下nginx，发布系统，测试，修改
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    waitupdate = issue.host_issue_set
    rd = random.randint(0, int(waitupdate.count()) - 1)  # 任选一台
    waithost = waitupdate.all()[rd]
    file_path = '/backup' + issue.team.path + issue.src_path
    if issue.type == "0":
        src_path = '/upload'+issue.team.path + issue.src_path
    else:
        src_path = '/upload'+ issue.team.path
    nginx(issue, waithost.host.hostip, 1)  # 摘nginx
    print(src_path)
    service(src_path, file_path, issue.team.path, [waithost], type=1)
    waithost.status = "2"
    waithost.save()
    issue.status = "2"
    issue.path = file_path
    issue.save()
    return redirect(reverse("updateall"))


def update_again(request, pk):
    """
    发布剩余机器
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    waitupdate = Host_Issue.objects.filter(issue=issue, status="0")
    for waithost in waitupdate.all():
        nginx(issue, waithost.host.hostip, 1)
        waithost.status = "2"
        waithost.save()
    if issue.type == "0":
        src_path = '/upload' + issue.team.path + issue.src_path
    else:
        src_path = '/upload' + issue.team.path
    service(src_path,issue.path, issue.team.path, waitupdate.all(), type=1)
    issue.status = "2"
    issue.save()
    return redirect(reverse("updateall"))


def successful(request, pk):
    """
    确认更新，当所有的都改成更新以后，直接改变总的为更新
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    host_issue = Host_Issue.objects.filter(issue=issue, status="2")
    for hi in host_issue:
        hi.status = "3"
        hi.save()
    issue.status = "3"
    issue.save()
    host_issue_again = Host_Issue.objects.filter(issue=issue, status="0")
    if host_issue_again.count() == 0:
        issue.status = "4"
        issue.save()
    return redirect(reverse("updateall"))


def backup(request, pk):
    issue = Issue.objects.filter(pk=pk).first()
    waithosts = Host_Issue.objects.filter(issue=issue, status="3")
    for waithost in waithosts:
        waithost.status = "6"
        waithost.save()
    issue.status = "6"
    issue.save()
    return redirect(reverse("updateall"))


def nginx(item, host, type=1):
    """
    摘nginx 重启nginx 挂载nginx
    :type 1摘nginx 0 挂载nginx
    :return:
    """
    nginxhosts = item.team.nginxhost.all()
    tasks = []
    if type == 1:
        replace_nginx = {"action": {"module": "replace",
                                    "args": 'path={} regexp="^({}.*)" replace="#\\1"'.format(item.team.nginxconf,host)},
                         "name": "down nginx"}
    else:
        replace_nginx = {"action": {"module": "replace",
                                    "args": 'path={} regexp="^#({}.*)" replace="\\1"'.format(item.team.nginxconf,host)},
                         "name": "down nginx"}
    restart_nginx = {"action": {"module": "service", "args": 'name=nginx state=reload'}, "name": "reload nginx"}
    tasks.append(replace_nginx)
    tasks.append(restart_nginx)
    host_data = [{"hostname": ng.hostip, 'ip': ng.hostip, 'user': 'root'} for ng in nginxhosts]
    inventory = Inventory(host_data)
    runner = AdHocRunner(inventory)
    runner.run(tasks)


def service(src_path, backup_path, path, host_list, type=1):
    """
    后端服务器操作
    :param filepath 文件地址
    :param path 项目目录
    :param host: 对应的主机
    :param type: 1更新 2回滚
    :return:
    """
    tasks = []
    if type == 1:
        backup = {"action": {"module": "shell", "args": "cp -rf {} {}".format(path, backup_path)}, #硬连接不能实现
                  "name": "backup file"}
        task = {"action": {"module": "copy", "args": "dest={},src={}".format(path, src_path)},
                "name": "copy file"}  # 复制本地文件到远程
        tasks.append(backup)
    else:
        task = {"action": {"module": "shell", "args": "cp -rf {} {}".format(backup_path, path)}, "name": "goback"}  # 回滚
    tasks.append(task)
    print([host.team.name for host in host_list])
    host_data = [{"hostname": host.host.hostip, 'ip': host.host.hostip, 'user': 'root'} for host in host_list]
    print(host_data, tasks)
    inventory = Inventory(host_data)
    runner = AdHocRunner(inventory)
    runner.run(tasks)
