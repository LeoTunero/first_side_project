from django.views.generic import DetailView, ListView

from post.models import Post


class PostListView(ListView):

    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'
