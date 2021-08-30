from django.db import models


class Car(models.Model):
    car_brand = models.TextField()
    car_model = models.TextField()

    class Meta:
        db_table = 'car'
