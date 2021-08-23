from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class car(models.Model):
    class Meta:
        db_table = '/Users/leo/Documents/python_test/leo_first_python_side_project/sharky/car.csv'
    id = models.IntegerField(primary_key=True)
    car_brand = models.CharField(max_length=20, default='Honda')
    car_model = models.TextField(default='EK9')
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_brand
