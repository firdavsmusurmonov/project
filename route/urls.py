# import avatar as avatar
from rest_framework import routers

from account.views import *


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
                  path('registr', registr),
                  path('me', Me.as_view({'get': 'list'})),
                  path('meee', me),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += router.urls
