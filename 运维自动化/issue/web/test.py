#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, redirect, reverse
from .test_forms import TestCreateForm
from .models import Test
from django.http import JsonResponse
import re
import subprocess


def test_all(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {"page_title": "压力测试", "tests": tests, 'user': request.account})


def test_create(request):
    test_obj = TestCreateForm()
    if request.method == "POST":
        test_obj = TestCreateForm(request.POST)
        if test_obj.is_valid():
            out = subprocess.getoutput(
                'siege -r{0} -c{1} "{2}" >/tmp/siege.log'.format(test_obj.cleaned_data['bingfa'],
                                                                 test_obj.cleaned_data['num'],
                                                                 test_obj.cleaned_data['url']))
            test_obj.instance.allnum = re.findall("Transactions:(.*)hits", out, re.S)[0].strip()  # 完成总次数请求
            test_obj.instance.cgl = re.findall("Availability:(.*)Elapsed time:", out, re.S)[0].strip()  # 成功率
            test_obj.instance.alltime = re.findall("Elapsed time:(.*)Data transferred:", out, re.S)[0].strip()  # 总用时
            test_obj.instance.data = re.findall("Data transferred:(.*)Response time:", out, re.S)[0].strip()  # 传输数据
            test_obj.instance.response = re.findall("Response time:(.*)Transaction rate:", out, re.S)[0].strip()  # 响应时间
            test_obj.instance.rate = re.findall("Transaction rate:(.*)Throughput:", out, re.S)[0].strip()  # 平均每秒完成的请求次数
            test_obj.instance.throughput = re.findall("Throughput:(.*)Concurrency:", out, re.S)[0].strip()  # 每秒传输的数据
            test_obj.instance.concurrency = re.findall("Concurrency:(.*)Successful transactions:", out, re.S)[
                0].strip()  # 实际最高并发连接数
            test_obj.instance.successful = re.findall("Successful transactions:(.*)Failed transactions:", out, re.S)[
                0].strip()  # 成功次数
            test_obj.instance.failed = re.findall("Failed transactions:(.*)Longest transaction:", out, re.S)[
                0].strip()  # 失败次数
            test_obj.save()
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(test_obj.errors)})
    return render(request, 'test_create.html', {'form': test_obj})


def test_delete(request, pk):
    Test.objects.filter(pk=pk).delete()
    return redirect(reverse('testall'))


def test_detail(request, pk):
    obj = Test.objects.filter(pk=pk).first()
    return render(request, 'test_detail.html', {'test': obj})
