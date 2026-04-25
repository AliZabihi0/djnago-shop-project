from django import forms



class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    subject = forms.CharField()
    message = forms.CharField()
    