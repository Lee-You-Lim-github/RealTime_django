from django.contrib import admin
from user.models import Black, Pick


@admin.register(Black)
class BlackAdmin(admin.ModelAdmin):
    pass


@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
    pass
