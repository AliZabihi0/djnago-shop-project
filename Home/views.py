from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from Home.forms import ContactForm


# Create your views here.
class Home(TemplateView):
    template_name = "home/index.html"

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "product/contact.html"
