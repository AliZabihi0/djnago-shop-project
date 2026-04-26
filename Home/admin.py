from multiprocessing.resource_tracker import register

from django.contrib import admin

from Home.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ("مشخصات", {'fields': ('name', 'email',)}),
        ("موضوع", {'fields': ('subject',)}),
        ("پیام", {'fields': ('message',)}),
    ]
    list_display = ['name', 'email', 'subject']

