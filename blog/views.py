from typing import Any

from blog.data import posts
from django.http import Http404, HttpRequest
from django.shortcuts import render


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

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        # 'text': 'Olá blog',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context
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
