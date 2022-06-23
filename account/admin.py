from django.contrib import admin

# Register your models here.

from account.models import Customuser, Region, Passport


class CustomuserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id','name_uz','name_ru','name_en']

class PassportAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Customuser, CustomuserAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Passport, PassportAdmin)
