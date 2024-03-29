from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name   = models.CharField(verbose_name='Nombre', max_length=100)
    update = models.DateField(verbose_name='Fecha de actualización', auto_now=True)
    create = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name        = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering            = ['-create']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title        = models.CharField(verbose_name='Titulo', max_length=250)
    content      = models.TextField(verbose_name='Contenido')
    date_publish = models.DateField(verbose_name='Fecha de publicación', default=timezone.now)
    image        = models.ImageField(verbose_name='Imagen', upload_to='post', null=True, blank=True)
    autor        = models.ForeignKey(User, verbose_name='Autor',on_delete=models.CASCADE)
    categories   = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_post')
    update       = models.DateField(verbose_name='Fecha de actualización', auto_now=True)
    create       = models.DateField(verbose_name='Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title
    