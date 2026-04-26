from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=100, verbose_name="عنوان")
    message = models.TextField(verbose_name="پیام")

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"
