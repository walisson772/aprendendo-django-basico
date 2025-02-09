from django.shortcuts import render


# Create your views here.
def blog(request):
    context = {
            'text': 'Estou no blog',
            'title': 'Blog - ',
        }
    return render(
        request,
        'blog/index.html',
        context,
    )

def exemplo(request):
    context = {
            'text': 'Estou mudando o texto',
            'title': 'Exemplo - '
        }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )