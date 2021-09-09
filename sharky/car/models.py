from django.db import models
from django.contrib import admin


class Car(models.Model):
    brand = models.TextField(default='Honda')
    model = models.TextField(default='EK9')

    class Meta:
        db_table = 'car'

    def __str__(self):
        return self.model
