from django.db import models

# Create your models here.
class Service(models.Model):
    title     = models.CharField(verbose_name='Titulo', max_length=200)
    subtitle  = models.CharField(verbose_name='Subtitulo', max_length=200)
    content   = models.TextField(verbose_name='Descripción')
    link      = models.URLField(verbose_name='Link referencia')
    image     = models.ImageField(verbose_name='Imagen', upload_to='services')
    create    = models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    update    = models.DateTimeField(verbose_name='Fecha de modificación',auto_now=True)

    class Meta:
        verbose_name        = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-create']
    
    def __str__(self):
        return self.title
    