from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

app_name = "shop"

router = DefaultRouter()
router.register("shops", views.ShopViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]