from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse

# Create your views here.
from .models import UserProfile


def login(request):
    error_msg = ''
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserProfile.objects.filter(email=email, password=password).first()
        if user:
            request.session["user_id"] = user.pk
            return redirect(reverse('updateall'))
        error_msg = "用户名或密码错误"
    return render(request, 'login.html', {"error_msg": error_msg})


def logout_view(request):
    request.session.flush()
    return redirect(reverse('login'))


def index(request):
    return render(request, 'project_list.html', {'page_title': "项目列表"})
