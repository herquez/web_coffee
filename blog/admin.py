from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    ordering = ('name',)
    search_fields = ('name',)
    date_hierarchy = 'created'

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'categories_list', 'author', 'published', 'created', 'updated')
    ordering = ('published', 'author')
    search_fields = ('title', 'content', 'author', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def categories_list(self, obj):
        return ','.join([category.name for category in obj.categories.all().order_by('name')])
    categories_list.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)