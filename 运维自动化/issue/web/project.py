#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, redirect, reverse
from .models import Team
from .project_forms import ProjectCreateForm
from django.http import JsonResponse
from django.db.models import Q


def project_all(request):
    name = request.GET.get('name', '')
    teams = Team.objects.filter(
        Q(name__contains=name, user_id=request.account) | Q(name__contains=name, test_user=request.account))
    return render(request, 'project_list.html', {"page_title": "项目列表", "teams": teams, 'user': request.account})


def project_create(request, pk=0):
    obj = Team.objects.filter(pk=pk).first()
    pro_obj = ProjectCreateForm(instance=obj)
    if request.method == "POST":
        pro_obj = ProjectCreateForm(request.POST, instance=obj)
        if pro_obj.is_valid():
            print(pro_obj.cleaned_data)
            pro_obj.save()
            return JsonResponse({'status': 0, 'msg': "操作成功！"})
        else:
            return JsonResponse({'status': 1, 'msg': "操作失败！,{}".format(pro_obj.errors)})
    return render(request, 'project_create.html', {'form': pro_obj, 'pk': pk})


def project_delete(request, pk):
    Team.objects.filter(pk=pk).delete()
    return redirect(reverse('projectall'))


def team_detail(request, pk):
    obj = Team.objects.filter(pk=pk).first()
    return render(request, 'team_detail.html', {'team': obj})
