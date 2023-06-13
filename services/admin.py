from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'content', 'image', 'created', 'updated')
    ordering = ('created',)
    search_fields = ('title', 'subtitle')
    date_hierarchy = ('created')

admin.site.register(Service, ServiceAdmin)
