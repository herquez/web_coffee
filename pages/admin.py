from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'deleted')
    list_display = ('title', 'order')
    ordering = ('order',)
    search_fields = ('title', 'content')
    date_hierarchy = ('created')

admin.site.register(Page, PageAdmin)