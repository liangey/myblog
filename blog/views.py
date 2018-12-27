from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

#def index(requset):
#   return render(requset,'index.html')


def index(request):
    articles=models.Article.objects.get(pk=1)
    return render(request,'index.html',{'articles':articles})


def article_page(request,article_id):
    article_id=models.Article.objects.get(pk=article_id)
    return render(request,'article_page.html',{'article':article})