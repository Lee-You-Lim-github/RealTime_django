from django.urls import path, include
from rest_framework.routers import DefaultRouter
from review import views

app_name = "Review"

router = DefaultRouter()
router.register("review", views.ReviewViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]