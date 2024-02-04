from django.shortcuts import render, redirect, HttpResponse

from .libs.corelib import request_get

@request_get
def index(request):
    return render(request, 'core/index.html')

@request_get
def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

@request_get
def sample(request):
    return render(request, 'core/sample.html')

@request_get
def store(request):
    return render(request, 'core/store.html')