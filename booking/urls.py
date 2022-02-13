from django.urls import path, include
from rest_framework.routers import DefaultRouter

from booking import views

app_name = "booking"

router = DefaultRouter()
router.register("newbooking", views.BookingCreateViewSet)
router.register("bookings", views.BookingReadViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]