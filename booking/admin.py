from django.contrib import admin
from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass