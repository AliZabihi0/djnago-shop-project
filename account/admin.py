from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
from .models import User, Address

class AddressAdmin(admin.TabularInline):
    model = Address


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    inlines = (AddressAdmin,)

    list_display = ('phone', 'is_admin',)
    list_filter = ('is_admin','is_active')
    fieldsets = (
        (None, {'fields': ('phone','email', 'password')}),
        ("اطلاعات شخصی", {'fields': ('first_name','last_name',)}),
        ("دسترسی ها", {'fields': ('is_admin',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','email', 'password1', 'password2','first_name','last_name','is_admin')
        }),

    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()



admin.site.unregister(Group)
