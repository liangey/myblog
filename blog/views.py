from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requset):
    return HttpResponse('This is my blog')