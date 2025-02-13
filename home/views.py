from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
            'text': 'Estou na home',
            'title': 'Home - ',
        }
    
    return render(
        request,
        'home/index.html',
        context
    )
