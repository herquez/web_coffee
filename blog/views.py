from django.shortcuts import render
from .models import Post as Post_mdl

def blog(request):
    posts = Post_mdl.objects.filter(deleted__isnull = True)
    context = {
        'posts_all': posts
    }
    return render(request, 'blog/blog.html', context)