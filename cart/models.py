from datetime import timezone

from django.db import models
from django.utils.text import slugify

from account.models import User
from product.models import Product, Size, Color


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    slug = models.SlugField(unique=True , max_length=100)
    total = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.phone)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.email}-{self.user.phone}'

    class Meta:
        verbose_name_plural = "سفارش"
        verbose_name = "سفارش ها"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.IntegerField(verbose_name="تعداد")
    size = models.CharField(verbose_name="سایز")
    color = models.CharField(verbose_name="رنگ")
    price = models.IntegerField(verbose_name="قیمت")

    def __str__(self):
        return f'{self.product.name}-{self.size}-{self.color}'

    class Meta:
        verbose_name_plural = "ایتم"
        verbose_name = "ایتم ها"


class DiscountCode(models.Model):
    name = models.CharField(max_length=20 , unique=True, verbose_name="کد")
    discount = models.SmallIntegerField(default=0, verbose_name="تخفیف")
    quantity = models.SmallIntegerField(default=0, verbose_name="تعداد")
    def __str__(self):
        return f'{self.name}-{self.discount}'

    class Meta:
        verbose_name =  "کد تحفیف"
        verbose_name_plural = "کد های تخفیف"