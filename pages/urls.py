from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:pageid>', views.page, name='page')
]
