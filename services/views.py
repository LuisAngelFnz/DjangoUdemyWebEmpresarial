from django.shortcuts import render

from core.libs.corelib import request_get
from .models import Service
@request_get
def services(request):
    services = Service.objects.all()
    return render(
        request,
        'services/services.html',
        {'services':services}
    )