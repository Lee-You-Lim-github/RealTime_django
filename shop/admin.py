from django.contrib import admin
from shop.models import Shop, Review


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass