from django import forms
from django import forms


class ContactForm(forms.Form):
    name     = forms.CharField( error_messages = {
                 'required':"Debes ingresar el nombre"
                 })
    email    = forms.EmailField(required=True)
    subject  = forms.CharField(required=True)
    phone    = forms.CharField(required=True)
    message  = forms.CharField(widget=forms.Textarea, required=True)
