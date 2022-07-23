from django.contrib.auth.models import AbstractUser
from django.db import models


def get_avatar(instance, filename):
    return "users/%s" % (filename)


def get_avatar_wife(instance, filename):
    return "users/%s" % (filename)


# class Region(models.Model):
#     objects = None
#     name = models.CharField(max_length=255)
#     parent = models.ForeignKey('self', related_name="childs", blank=True, null=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
# class Region(models.Model):
#     name_uz = models.CharField(max_length=255, blank=True)
#     name_ru = models.CharField(max_length=255, blank=True)
#     name_en = models.CharField(max_length=255, blank=True)
#     parent = models.ForeignKey('self', blank=True, null=True, related_name='childs', on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.name_uz
#
#
# class Education(models.Model):
#     name = models.CharField(max_length=225, null=True)
#
#     def __str__(self):
#         return self.name
#
#
class Family(models.Model):
    name = models.CharField(max_length=255, default="uylanmagan", null=True)

    def __str__(self):
        return self.name


class Customuser(AbstractUser):
    GENDER_CHOICES = (
        ('man', 'Man'),
        ('woman', ' Woman')
    )
    smscode = models.IntegerField(default=0)
    complete = models.IntegerField(default=0)
    first_name = models.CharField(max_length=150, unique=False, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=get_avatar, default='users/default.png')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, blank=True)
    date = models.CharField(max_length=150, unique=False, blank=True, null=True)
    month = models.CharField(max_length=150, unique=False, blank=True, null=True)
    year = models.CharField(max_length=150, unique=False, blank=True, null=True)
    region_birth = models.CharField(max_length=150, unique=False, blank=True, null=True)
    city_birth = models.CharField(max_length=150, unique=False, blank=True, null=True)
    region = models.CharField(max_length=150, unique=False, blank=True, null=True)
    city = models.CharField(max_length=150, unique=False, blank=True, null=True)
    fulladress = models.CharField(max_length=150, null=True)
    passport = models.CharField(max_length=150, null=True)
    passport_date = models.CharField(max_length=150, unique=False, blank=True, null=True)
    passport_month = models.CharField(max_length=150, unique=False, blank=True, null=True)
    passport_year = models.CharField(max_length=150, unique=False, blank=True, null=True)
    education = models.CharField(max_length=150, unique=False, blank=True, null=True)
    family = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_first_name = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_last_name = models.CharField(max_length=150, blank=True, null=True)
    wife_gender = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, blank=True)
    wife_date = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_month = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_year = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_region_birth = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_city_birth = models.CharField(max_length=150, unique=False, blank=True, null=True)
    wife_avatar = models.ImageField(upload_to=get_avatar_wife, default='users/default.png')
    wife_education = models.CharField(max_length=150, unique=False, blank=True, null=True)
    childs = models.CharField(max_length=150, unique=False, blank=True, null=True)


class Order(models.Model):
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE, related_name='user_or')
    price = models.CharField(max_length=200,null=True, blank=True, default=0)
    create_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='order_0',on_delete=models.CASCADE)
    price = models.CharField(max_length=200, null=True, blank=True, default=0)
    def __str__(self):
        return str(self.price)
