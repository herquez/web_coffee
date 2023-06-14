from django.shortcuts import render, get_object_or_404
from .models import Post as Post_mdl
from .models import Category as Category_mld

def blog(request):
    posts = Post_mdl.objects.filter(deleted__isnull = True)
    context = {
        'posts_all': posts
    }
    return render(request, 'blog/blog.html', context)

def category(request, category_id):
    category = get_object_or_404(Category_mld, id=category_id, deleted__isnull=True)
    context = {
        'category': category,
    }
    return render(request, 'blog/category.html', context)