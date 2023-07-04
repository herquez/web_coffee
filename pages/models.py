from django.db import models

class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)
    deleted = models.DateTimeField(verbose_name='Fecha de eliminación', blank=True, null=True)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['Title']

    def __str__(self):
        return self.title
    