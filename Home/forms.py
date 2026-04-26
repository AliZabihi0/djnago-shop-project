from django import forms

from Home.models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل شما'}),
            "subject": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع شما'}),
            "message": forms.Textarea(attrs={'class': 'form-control','placeholder': 'پیام خود را بنویسید'}),
        }

