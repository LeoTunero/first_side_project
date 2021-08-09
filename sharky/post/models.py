from django.db import models


class Post(models.Model):

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essay'

    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title
