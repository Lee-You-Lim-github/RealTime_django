from django.contrib import admin
from shop.models import Shop, Conv, Review


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Conv)
class ConvAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass