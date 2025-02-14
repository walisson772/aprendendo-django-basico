from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
