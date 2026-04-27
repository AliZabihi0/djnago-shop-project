from django.contrib import admin
from django.core.checks import Info

from product.models import Product, Size, Color, Information, Category, Comment


class InformationAdmin(admin.StackedInline):
    model = Information



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets=[
        ("جزئیات محصول", {'fields': ('name', 'description', 'image','category')}),
        ("ویژگی های محصول", {'fields': ('size', 'color',)}),
        ("قیمت", {'fields': ('price','discount','price_discount')}),
        ("موجودیت", {'fields': ('available',)}),
    ]
    list_display = ['name','price','available','id']
    inlines = [InformationAdmin]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ("مشخصات", {'fields': ('author',)}),
        ("موضوع", {'fields': ('post','body')}),
        ("ریپلای", {'fields': ('parent',)}),
    ]
    list_display = ['author', 'post', 'body']



admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)