from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Address
from django.core.validators import MaxLengthValidator, MinValueValidator


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='گذرواژه', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return self.cleaned_data.get("password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'email', 'is_admin', "password", 'first_name','last_name')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mt-1 '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1'}))


class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mt-1'}),
                            validators=[MaxLengthValidator(11)])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-1'}))

    def clean(self):
        cd = super(RegisterForm, self).clean()
        password1 = cd['password1']
        password2 = cd['password2']
        if password1 != password2:
            raise ValidationError("پسورد یکسان نیست", code='dont_match')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise ValidationError("کاربر از قبل وجود دارد")
        return phone

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'address')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'phone': forms.TextInput(attrs={'class': 'form-control '}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:

        model = Address
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-1','placeholder':'نام' }),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-1','placeholder':'نام خانوداگی'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1','placeholder':'ایمیل'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-1','placeholder':'تلفن'}),
            'address': forms.TextInput(attrs={'class': 'form-control mt-1','placeholder':'آدرس'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control mt-1','placeholder':'کد پستی'}),

        }

