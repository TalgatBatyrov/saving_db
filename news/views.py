from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse("Hello World News")


def test(request):
    #  red color h1 text 
    return HttpResponse('<h1 style="color:red">Hello World News</h1>')