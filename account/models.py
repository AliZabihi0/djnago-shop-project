from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Users must have an phone number')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        user = self.create_user(phone, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True, verbose_name="تلفن")
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True, error_messages={
        'unique': "A user with that email already exists.",
    }, verbose_name='ایمیل')
    first_name = models.CharField(max_length=20,blank=True,null=True,verbose_name="نام")
    last_name = models.CharField(max_length=20,blank=True,null=True,verbose_name="نام خانوادگی")
    address= models.CharField(max_length=100,blank=True,verbose_name="ادرس")
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")
    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11,unique=True)
    code = models.IntegerField()
    password = models.CharField(max_length=128)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='addresses',verbose_name='کاربر')
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=100, verbose_name="تلفن")
    address = models.CharField(max_length=100, verbose_name="آدرس")
    zipcode = models.CharField(max_length=100, verbose_name="کدپستی")

    def __str__(self):
        return self.user.phone


    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"