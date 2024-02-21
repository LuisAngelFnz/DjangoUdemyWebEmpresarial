from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', min_length=10, max_length=50, required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'}
    ))
    email = forms.EmailField(label='Correo Electrónico', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ))
    content = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Escribe tu mensaje',
            'rows':'3'
        }
    ))