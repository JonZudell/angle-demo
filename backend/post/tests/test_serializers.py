from django.test import TestCase
from ..serializers import PostSerializer
from ..models import Post
class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(**{"name" : "example", "start_date" : "09/04/2022", "price" : 0})
        self.serializers = PostSerializer(instance=self.post)
    
    def test_serialize(self):
        pass
    
    def test_deserialize(self):
        pass