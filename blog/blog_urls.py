#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2018-12-26 17:33
#@Author: ley
#@Site : 
#@File : blog_urls.py
#@Software : PyCharm


from django.conf.urls import url
from . import views

urlpatterns = [
    url('index/',views.index),
]