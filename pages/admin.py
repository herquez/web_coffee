from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'deleted')
    list_display = ('title', 'content', 'created', 'updated')
    ordering = ('created',)
    search_fields = ('title', 'content')
    date_hierarchy = ('created')

admin.site.register(Page, PageAdmin)