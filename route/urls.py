from rest_framework import routers

from account.views import *

router = routers.DefaultRouter()

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homepage, name='home'),
    path('registr', registr),
    path('me', me),
    path('region', region),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += router.urls
