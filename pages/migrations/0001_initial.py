# Generated by Django 5.0.1 on 2024-02-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'pagina',
                'verbose_name_plural': 'paginas',
                'ordering': ['title'],
            },
        ),
    ]
