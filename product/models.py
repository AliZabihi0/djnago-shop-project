from tabnanny import verbose

from django.db import models

from account.models import User
from jalali_date_new.fields import JalaliDateTimeField, JalaliDateField
from jalali_date_new.widgets import AdminJalaliDateTimeWidget, AdminJalaliTimeWidget, AdminJalaliDateWidget


class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'سایز ها '
        verbose_name = 'سایز'


class Color(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'رنگ ها '
        verbose_name = 'رنگ'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    price = models.BigIntegerField(verbose_name="قیمت")
    price_discount = models.BigIntegerField(verbose_name="قیمت با تخفیف")
    discount = models.SmallIntegerField(verbose_name="تخفیف")
    image = models.ImageField(upload_to='products', verbose_name="تصویر محصول")
    size = models.ManyToManyField(Size, related_name='product', verbose_name="سایز")
    color = models.ManyToManyField(Color, related_name='product', verbose_name="رنگ")
    available = models.BooleanField(default=True, verbose_name="موجود")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")

    def save(self, *args, **kwargs):
        self.price_discount = self.price - (self.price * self.discount / 100)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'


class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="informations")
    title = models.CharField(max_length=300, verbose_name="عنوان ")
    text = models.TextField(verbose_name="متن ")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'مشخصات محصولات'
        verbose_name = 'مشخصات'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="نویسنده")
    body = models.TextField(verbose_name="متن")
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", verbose_name="پست")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies",
                               verbose_name="پدر")
    created = JalaliDateTimeField()

    class Meta:
        verbose_name_plural = 'نظرات'
        verbose_name = 'نظر'

    def __str__(self):
        return f"{self.author} - {self.body}"

