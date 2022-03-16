from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop import views

app_name = "shop"

router = DefaultRouter()
router.register("newshop", views.ShopCreateViewSet)
router.register("shops", views.ShopReadViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

]