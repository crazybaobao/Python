"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from blog import views
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

urlpatterns = [
    path('admin/', admin.site.urls),  # 管理后台
    path('', views.index, name='index'),  # 网站首页
    path('list-3.html/', views.list_3),  # Python页
    path('list-5.html', views.show_ops),  # 运维页
    path('list-6.html', views.show_daily),  # 日记页
    path('list-2.html', views.list_2),  # 手账页
    path('about/', views.about),  # 关于我单页
    path('ueditor/', include('DjangoUeditor.urls')),
    path('base.html', views.jenkin),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
