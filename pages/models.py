from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title   = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    order   = models.SmallIntegerField(verbose_name='Order', default=0)
    create  = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    update  = models.DateTimeField(verbose_name='Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order','title']

    def __str__(self):
        return self.title
