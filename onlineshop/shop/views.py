from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.
catalog = 'shop/'
menu = ["Головна сторінка", "Пошук по сайту", "Вхід"]


def index(request):
    book_list = Unit.objects.all()
    return render(request, catalog + 'index.html', {'menu': menu, 'title': 'OnlineShop', 'books': book_list})


def about(request):
    return render(request, catalog + 'about.html', {'menu': menu, 'title': 'OnlineShopAbout'})


def categories(request, catid):
    if request.GET:
        print(request.GET)

    if catid > 20:
        return redirect('main', permanent=False)

    return HttpResponse(f"<h1>Categories! {catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found!</h1>")