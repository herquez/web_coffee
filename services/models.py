from django.db import models

class Service(models.Model):
    title = models.CharField(verbose_name='titulo', max_length=200)
    subtitle = models.CharField(verbose_name='subtitulo', max_length=200)
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to='services')
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now=True) 
    deleted = models.DateField(verbose_name='Eliminado', blank=True, null=True, editable=False)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title