# import avatar as avatar
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from account.views import *

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from click.api.views import ClickUzMerchantAPIView, ClickGenereteUrl

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
                  path('registr', registr),
                  path('me', Me.as_view({'get': 'list'})),
                  path("update-img", update_profil_img),
                  path('click', csrf_exempt(ClickUzMerchantAPIView.as_view())),
                  path('click-url/', ClickGenereteUrl.as_view()),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += router.urls
