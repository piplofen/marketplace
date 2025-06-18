from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .utils import *

def index(request):
    context = {
        "title": "Главная"
    }
    return render(request, "basic/index.html", context=context)

class ItemHome(DataMixin, ListView):
    model = Item
    template_name = "basic/item_list.html"
    context_object_name = "items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        more_context = self.get_user_content(title="Товары")

        return dict(list(context.items( )) + list(more_context.items()))

def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "basic/contacts.html", context=context)

def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "basic/about.html", context=context)