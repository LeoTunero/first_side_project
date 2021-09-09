from django.contrib import admin
from rest_framework.renderers import AdminRenderer

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model')
