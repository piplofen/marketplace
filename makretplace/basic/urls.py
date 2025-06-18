from django.contrib import admin
from django.urls import path, include

from .views import *
from basic import views

urlpatterns = [
    path('', views.index, name="home"),
    path('items/', ItemHome.as_view(), name="item"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),
]
