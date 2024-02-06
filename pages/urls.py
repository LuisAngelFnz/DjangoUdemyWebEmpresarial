from django.urls import path
from . import views

urlpatterns = [
    path('<int:pageid>/<slug:slug_title>', views.page, name='page')
]
