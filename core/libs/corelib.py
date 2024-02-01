from django.shortcuts import redirect

def request_get(function):
    def fwrap(request, **args):
        if request.method == 'GET':
            return function(request, **args)
        elif function.__name__ != 'index':
            return redirect('index')
        else:
            return redirect(function.__name__)
    return fwrap
