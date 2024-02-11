from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        objform = ContactForm(data=request.POST)
        print(objform.is_valid())
        if objform.is_valid():
            name, email, content = map(request.POST.get, ('name','email','content'))
            #Todo ok
            return redirect('/contact/?ok')
    else:
        objform = ContactForm()
    # objform = ContactForm()
    return render(request, 'contact/contact.html', {'form':objform})