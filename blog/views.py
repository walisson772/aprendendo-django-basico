from django.shortcuts import render
from blog.data import posts


# Create your views here.
def blog(request):
    context = {
            'text': 'Estou no blog',
            'title': 'Blog - ',
            'posts': posts
        }
    return render(
        request,
        'blog/index.html',
        context,
    )

def post(request, id):
    found_post = None

    for post in posts:
        if post['id'] == id:
            found_post = post
            break

    context = {
            'post': found_post
        }
    return render(
        request,
        'blog/postblock.html',
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
