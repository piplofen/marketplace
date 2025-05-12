from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, "main.html", context=context)

def items(request):
    context = {
        'title': 'Товары'
    }
    return render(request, 'items.html', context=context)

def contacts(request):
    context = {
        'title': "Контакты"
    }
    return render(request, 'contacts.html', context=context)

def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, "about.html", context=context)

def pageNotFound(request, exception):
    return HttpResponse("Unfortunately page not found(")