from multiprocessing.resource_tracker import register

from django.contrib import admin

from Home.models import Message

# Register your models here.
admin.site.register(Message)