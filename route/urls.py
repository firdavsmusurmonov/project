# import avatar as avatar
from rest_framework import routers

from account.views import *

router = routers.DefaultRouter()

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', homepage, name='home'),
                  path('avatar', avatar, name='avatar'),
                  path('registr', registr),
                  path('me', Me.as_view({'get': 'list'})),
                  path('region', region),
                  path('update-profil-img', update_profil_img),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += router.urls
