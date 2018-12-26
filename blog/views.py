from .models import Category

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Article


# 首页
def index(request):
    allcategory = Category.objects.all()
    context = {'allcategory': allcategory, }
    return render(request, 'index.html', context)


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
