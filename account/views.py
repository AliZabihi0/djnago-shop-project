from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, CreateView
from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm, ProfileForm, AddressForm
from random import randint


from account.models import User, Address


# Create your views here.
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/')
        form.add_error("username", "موبایل/ایمیل یا پسورد وارد شده اشتباه است")
        return render(self.request, 'account/login.html', {'form': form})
    # def get(self, request):
    #     form = LoginForm()
    #     return render(request, 'account/login.html', {'form': form})
    #
    # def post(self, request):
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         phone = form.cleaned_data.get('phone')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request,username=phone, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('/')
    #         else:
    #             print(phone,password)
    #             form.add_error("phone","None data")
    #     else:
    #         form.add_error("phone","Get error")
    #     return render(request, 'account/login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(phone=phone, password=password)
            # login(request, user)
            return redirect('/')

        phone = form.cleaned_data.get('phone')
        print(phone)
        return render(request, 'account/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def edit_profile(request):
    user = request.user
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')

    return render(request, "account/profile.html", {'form': form})


class AddAddressView(View):

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            if Address.objects.filter(user=request.user).count() >= 10:
                form.add_error('first_name', "حداکثر مقدار مجار برای ثبت آدرس")
            else:
                address.save()
                next_page = request.GET.get('next')
                print(next_page)
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('account:list_address')
        return render(request, 'account/add_address.html', {'form': form})

    def get(self, request):
        form = AddressForm()
        return render(request, 'account/add_address.html', {'form': form})


class AddressListView(ListView):
    model = Address
    context_object_name = 'addresses'
    template_name = 'account/list_address.html'
