from django import template
from pages.models import Page as Page_mdl

register = template.Library()

@register.simple_tag
def get_pages():
    pages = Page_mdl.objects.filter(deleted__isnull=True)
    return pages