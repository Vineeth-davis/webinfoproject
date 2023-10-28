from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'platforms', views.PlatformViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
