from django.shortcuts import render
from django.http import HttpResponse
from .models import News



def index(request):
    news = News.objects.all()
    # res = '<h1>Список новостей</h1>'
    # print(dir(request))
    # print(news)

    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    # return HttpResponse(res)

    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей', })


def test(request):
    #  red color h1 text 
    return HttpResponse('<h1 style="color:red">Hello World Newss</h1>')