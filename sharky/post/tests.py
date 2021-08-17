from django.test import TestCase
from post.models import Post
import unittest


class PostTestCase(unittest.TestCase):
    def setUp(self):
        Post.objects.create(title='Test', content='whatever')
        Post.objects.create(title='Test_2', content='Idonotcare')
# I do not know what kind of test I could write before building any function
# So I have deceide that I should build the function before the test

    def test_can_run(self):
        # Try to run the unittest
        test = Post.objects.get(title='Test')
        test2 = Post.objects.get(title='Test2')
        self.assertNotEqual(test, test2)


if __name__ == '__main__':
    unittest.main()
