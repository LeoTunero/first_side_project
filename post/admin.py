from django.contrib import admin
from .models import Post
from .models import car
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')


@admin.site.register(car)
class carAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_brand', 'car_model',
                    'last_modify_date', 'created')
    search_fields = ('car_brand', 'car_model', 'last_modify_date', 'created')
