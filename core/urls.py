from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index ),
    path('index/',  views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
]