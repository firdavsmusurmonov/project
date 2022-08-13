from django.contrib import admin

# Register your models here.

from account.models import Customuser, Order, Region


class CustomuserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']


#
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent']


admin.site.register(Customuser, CustomuserAdmin)
admin.site.register(Order)

admin.site.register(Region, RegionAdmin)
# admin.site.register(Education)
# admin.site.register(Family)
