from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

app_name = "user"

router = DefaultRouter()
router.register("newblack", views.BlackCreateViewSet)
router.register("blacks", views.BlackReadViewSet)
router.register("newpick", views.PickCreateViewSet)
router.register("picks", views.PickReadViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]