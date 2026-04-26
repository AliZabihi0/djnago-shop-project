from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from Home.forms import ContactForm


# Create your views here.
class Home(TemplateView):
    template_name = "home/index.html"

class MessageComplete(TemplateView):
    template_name = "home/message-complete.html"

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "home/contact.html"
    success_url = reverse_lazy("home:message_complete")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
