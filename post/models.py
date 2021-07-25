from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    title = models.CharField('測試用的標題', max_length=20)
    content = models.CharField('第一次嘗試寫的內容', max_length=200)

    def __str__(self):
        return self.title
