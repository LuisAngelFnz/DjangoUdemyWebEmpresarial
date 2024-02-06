from django.urls import path
from . import views

urlpatterns = [
    path('<int:pageid>', views.page, name='page')
]
