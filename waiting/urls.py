from django.urls import path, include
from rest_framework.routers import DefaultRouter

from waiting import views

app_name = "waiting"

router = DefaultRouter()
router.register("waitings", views.WaitingViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]