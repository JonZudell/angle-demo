from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ..models import Post

class PostTestCase(TestCase):
    def test_post_create(self):
        """Model was created"""
        Post.objects.create(name="bar1", start_date="2022-09-04", price=1000)
        post = Post.objects.get(name="bar1")
        self.assertEqual(post.price, 1000)
    
    def test_post_create_fail_exists(self):
        Post.objects.create(name="bar1", start_date="2022-09-04", price=1000)
        with self.assertRaises(IntegrityError):
            Post.objects.create(name="bar1", start_date="2022-09-05", price=0)

    def test_model_create_fail_date(self):
        with self.assertRaises(ValidationError):
            Post(name="bar2", start_date="1960-09-05", price=0).clean_fields()

    def test_model_create_fail_name_short(self):
        with self.assertRaises(ValidationError):
            Post(name="", start_date="2022-09-05", price=0).clean_fields()

    def test_model_create_fail_name_long(self):
        with self.assertRaises(ValidationError):
            Post(name="01234567890", start_date="2022-09-05", price=0).clean_fields()

    def test_model_create_fail_name_invalid(self):
        with self.assertRaises(ValidationError):
            Post(name="?????", start_date="2022-09-05", price=0).clean_fields()