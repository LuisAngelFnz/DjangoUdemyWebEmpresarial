from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('',  views.index ),
    path('index/',  views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('store/', views.store, name='store'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    