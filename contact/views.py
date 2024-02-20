from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        objform = ContactForm(data=request.POST)
        print(objform.is_valid())
        if objform.is_valid():
            name, mail, content = map(request.POST.get, ('name','email','content'))
            # Enviar mensaje
            email = EmailMessage(
                'La Caffettiera : Nuevo mensaje de contacto',
                'De {} <{}> \n\nEscribio:\n\n{}'.format(name, mail, content),
                'no-contestar@inbox.mailtrap.io',
                ['lfernandez4gds@gmail.com'],
                reply_to=[mail]
            )
            try:
                email.send()
                return redirect('/contact/?ok')
            except:
                return redirect('/contact/?fail')
    else:
        objform = ContactForm()
    # objform = ContactForm()
    return render(request, 'contact/contact.html', {'form':objform})