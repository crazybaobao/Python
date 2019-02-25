import hashlib

from django.core.cache import cache
from django.urls import reverse
from django.views.decorators.http import etag

from decorator import ask_method
from .models import Category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from PIL import Image, ImageDraw
from io import BytesIO


class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            text = '{}*{}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)
        return content


def generate_etag(request, width, height):
    content = 'placeholder:{0}*{1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


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
    example = reverse('placeholder', kwargs={'width': 50, 'height': 50})
    context = {'example': request.build_absolute_uri(example)}
    return render(request, 'list-6.html', context)


# 手账
def list_2(request):
    return render(request, 'list-2.html')


# 关于我们
def about(request):
    return render(request, 'about.html')


# Jenkins页
def jenkin(request):
    return render(request, 'base.html')


# Ruby页
def rub(request):
    return render(request, 'ruby.html')


def djan(request):
    return HttpResponse('你好，世界！')


@etag(generate_etag)
def placeholder(request, width, height):
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')
