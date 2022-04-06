from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

app_name = "user"

router = DefaultRouter()
router.register("blacks", views.BlackViewSet)
router.register("blackLogs", views.BlackLogViewSet)
router.register("picks", views.PickViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]