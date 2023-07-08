from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(verbose_name='Fecha de creación', 
    auto_now_add=True)
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)
    deleted = models.DateTimeField(verbose_name='Fecha de eliminación', blank=True, null=True)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    