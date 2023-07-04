from django.shortcuts import render, get_object_or_404
from .models import Page as Page_mdl

def page(request, page_id):
    page = get_object_or_404(Page_mdl, id=page_id, deleted__isnull=True)
    context = {
        'page': page,
    }
    return render(request, 'pages/page.html', context)