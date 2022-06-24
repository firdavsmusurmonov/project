from rest_framework import routers

from account.views import *

router = routers.DefaultRouter()

from django.urls import path, include

urlpatterns = [
    path('', homepage, name='home'),
    path('registr', registr),
    path('me', me),
    path('region', region),
]
urlpatterns += router.urls
