from django.db import models


class Car(models.Model):
    car_brand = models.TextField()
    car_model = models.TextField()

    class Meta:
        db_table = 'car'

    def __str__(self):
        return self.car_model
