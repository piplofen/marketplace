from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('items', views.items, name='items'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
]
