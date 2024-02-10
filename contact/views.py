from django.shortcuts import render
from core.libs.corelib import request_get

@request_get
def contact(request):
    return render(request, 'contact/contact.html')