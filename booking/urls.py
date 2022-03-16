from django.urls import path, include
from rest_framework.routers import DefaultRouter

from booking import views

app_name = "booking"

router = DefaultRouter()
router.register("bookings", views.BookingViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]