from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع شما'}))
    message = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام خود را بنویسید'}))
