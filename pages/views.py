from django.shortcuts import render, get_object_or_404
from .models import Page
from core.libs.corelib import request_get

@request_get
def page(request, pageid):
    return render(
        request, 'pages/sample.html', {'page':get_object_or_404(Page, id=pageid)}
    )
