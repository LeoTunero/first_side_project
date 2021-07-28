from django.contrib import admin
from django.views.generic import ListView, DetailView
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


admin.site.register(Post, PostAdmin)
