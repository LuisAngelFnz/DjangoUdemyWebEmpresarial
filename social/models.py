from django.db import models

class Social(models.Model):
    key     = models.SlugField(verbose_name='Identificador', max_length=100, unique=True)
    name    = models.CharField(verbose_name='Red social', max_length=200)
    url     = models.URLField(verbose_name='Enlace', max_length=200, blank=True, null=True)
    create  = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    update  = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name        = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering            = ('-create',)
    
    def __str__(self):
        return self.name