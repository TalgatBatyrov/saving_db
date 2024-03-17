from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category



def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
   
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }

    return render(request,template_name= 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {
        'news': news,
        'category': category,
        'categories': categories
    }
    return render(request, template_name= 'news/category.html', context=context)


def test(request):
    #  red color h1 text 
    return HttpResponse('<h1 style="color:red">Hello World Newss</h1>')