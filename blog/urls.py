from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
