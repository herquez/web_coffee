from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red Social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now=True) 
    deleted = models.DateField(verbose_name='Eliminado', blank=True, null=True, editable=False)

    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Red social'
        ordering = ['name']

    def __str__(self):
        return self.name