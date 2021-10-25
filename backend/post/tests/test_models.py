from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ..models import Post

class PostTestCase(TestCase):
    #fixtures = ['data_01.json', 'data_02.json', 'data_03.json']
    def setUp(self):
        # django orm likes this date format. The view will convert to MM/DD/YYYY
        Post.objects.create(name="bar1", start_date="2022-09-04", price=1000)

    def test_post_create(self):
        """Model was created"""
        post1 = Post.objects.get(name="bar1")
        self.assertEqual(post1.price, 1000)
    
    def test_post_create_fail_exists(self):
        with self.assertRaises(IntegrityError):
            Post.objects.create(name="bar1", start_date="2022-09-05", price=0)

    def test_model_create_fail_date(self):
        with self.assertRaises(ValidationError):
            post1 = Post(name="bar2", start_date="1960-09-05", price=0)
            post1.clean_fields()