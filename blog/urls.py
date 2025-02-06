from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog),
    path('exemplo/', views.exemplo)
]
