from django.contrib import admin
from waiting.models import Waiting


@admin.register(Waiting)
class WaitingAdmin(admin.ModelAdmin):
    pass
