from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Train
# Create your views here.


def index(request):
    try:
        s = Train.objects.all()
        return HttpResponse(s)
    except:
        return HttpResponse("没有找到对应的信息！")
