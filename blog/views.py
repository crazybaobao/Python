from functools import wraps

from django.utils.log import log_response

from decorator import ask_method
from .models import Category
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseNotAllowed

from django.contrib.auth.models import User

from .models import Article


# 首页
@ask_method(['GET', 'POST'])
def index(request):
    allcategory = Category.objects.all()
    context = {'allcategory': allcategory, }
    return render(request, 'index.html', locals())


# Python页
def list_3(request):
    return render(request, 'list-3.html')


# 运维页
def show_ops(request):
    return render(request, 'html-5.html')


# 日记页
def show_daily(request):
    return render(request, 'list-6.html')


# 手账
def list_2(request):
    return render(request, 'list-2.html')


# 关于我们
def about(request):
    return render(request, 'about.html')


# Jenkins页
def jenkin(request):
    return render(request, 'base.html')
