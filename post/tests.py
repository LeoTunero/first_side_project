from django.test import TestCase
from post.models import Post

# Create your tests here.


class PostTestCase (TestCase):
    def setUp(self) -> None:
        Post.Meta.verbose_name = 'Essay'
        Post.Meta.verbose_name_plural = 'Essay'
        # return super().setUp()

    def test_post_title(self):
        # Test for practices only
        'Essay' = Post.Meta.verbose_name.capitalize
        'Essay' = Post.Meta.verbose_name_plural.capitalize
        print('test is passed')
