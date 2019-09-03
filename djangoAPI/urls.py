from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from suldocs.views import SuldocViewSet
from suldocs import views

router = routers.DefaultRouter()
router.register('suldocs', SuldocViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
]
