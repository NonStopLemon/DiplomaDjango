from django.contrib import admin
from .models import Fingers


@admin.register(Fingers)
class FingersAdmin(admin.ModelAdmin):
    pass
# Register your models here.
