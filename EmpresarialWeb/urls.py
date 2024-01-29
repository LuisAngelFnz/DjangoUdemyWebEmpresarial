"""
URL configuration for EmpresarialWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as coreviews

urlpatterns = [
    path('',  coreviews.index),
    path('index/',  coreviews.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', coreviews.about, name='about'),
    path('blog/', coreviews.blog, name='blog'),
    path('contact/', coreviews.contact, name='contact'),
    path('sample/', coreviews.sample, name='sample'),
    path('services/', coreviews.services, name='services'),
    path('store/', coreviews.store, name='store'),
]
