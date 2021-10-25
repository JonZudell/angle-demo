from django.test import TestCase
from .serializers import PostSerializer
from .models import Post
class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create({"id" : "example", "start_date" : "09/04/2022", "price" : 0})
        self.serializers = PostSerializer()