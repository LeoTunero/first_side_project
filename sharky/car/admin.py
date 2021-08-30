from django.contrib import admin
from rest_framework.renderers import AdminRenderer

from .models import Car


@admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_brand', 'car_model')
