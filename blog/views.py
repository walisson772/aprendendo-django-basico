from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse('blog do app cachorro 69')

def exemplo(request):
    return HttpResponse('Exemplo')