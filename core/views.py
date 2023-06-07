from django.shortcuts import render

def home(request):
    return render(request, 'core/contents/index.html')

def about(request):
    return render(request, 'core/contents/about.html')

def store(request):
    return render(request, 'core/contents/store.html')

def contact(request):
    return render(request, 'core/contents/contact.html')

def blog(request):
    return render(request, 'core/contents/blog.html')

def sample(request):
    return render(request, 'core/contents/sample.html')
