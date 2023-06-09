from django.shortcuts import render
from .models import Service as Service_mdl

def services(request):
    services_all = Service_mdl.objects.filter(deleted__isnull=True).order_by('created')
    context = {
        'services_all': services_all,
    }
    return render(request, 'services/services.html', context)