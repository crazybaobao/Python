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


# 列表页
def list(request, lid):
    pass


# 内容页
def show(request, sid):
    pass


# 标签页
def tag(request, tag):
    pass


# 搜索页
def search(request):
    pass


# 关于我们
def about(request):
    pass
