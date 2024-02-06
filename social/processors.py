from .models import Social

def context(request):
    return {'SOCIAL':Social.objects.all()}