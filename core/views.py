from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def rget(function):
    def fwrap(request, **args):
        if request.method == 'GET':
            return function(request, **args)
        elif function.__name__ != 'index':
            return redirect('index')
        else:
            return redirect(function.__name__)
    return fwrap

@rget
def index(request):
    return render(request, 'core/index.html')

@rget
def about(request):
    return render(request, 'core/about.html')

@rget
def blog(request):
    return render(request, 'core/blog.html')

def contact(request):
    return render(request, 'core/contact.html')

@rget
def sample(request):
    return HttpResponse('sample')
    return render(request, 'core/sample.html')

@rget
def services(request):
    return render(request, 'core/services.html')

@rget
def store(request):
    return render(request, 'core/store.html')