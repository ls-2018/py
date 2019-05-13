#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import render,reverse,redirect
from .models import *
from .user_forms import UserCreateForm
from django.http import JsonResponse

def user_all(request):
    name = request.GET.get('name', '')
    users = UserProfile.objects.filter(name__contains=name)
    return render(request, 'user_list.html', {"page_title": "人员列表", "users": users})


def user_create(request, pk=0):
    obj = User.objects.filter(pk=pk).first()
    user_obj = UserCreateForm(instance=obj)
    if request.method == "POST":
        user_obj = UserCreateForm(request.POST, instance=obj)
        if user_obj.is_valid():
            user_obj.save()
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(user_obj.errors)})
    return render(request, 'user_create.html', {'form': user_obj, 'pk': pk})


def user_delete(request, pk):
    UserProfile.objects.filter(pk=pk).delete()
    return redirect(reverse('projectall'))
