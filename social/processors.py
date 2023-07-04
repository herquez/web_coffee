from .models import Link as Link_mdl

def ctx_dict(request):
    links = Link_mdl.objects.filter(deleted__isnull=True)  
    ctx = {}
    for link in links:
        ctx[link.key] = link.url
    return ctx