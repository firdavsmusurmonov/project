from rest_framework import routers

from account.views import *

router = routers.DefaultRouter()

from django.urls import path, include

urlpatterns = [
    path('', homepage, name='home'),
]
urlpatterns += router.urls
