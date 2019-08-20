from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from suldocs.views import SuldocViewSet

router = routers.DefaultRouter()
router.register('suldocs', SuldocViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
