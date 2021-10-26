import io
from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers import PostSerializer
from ..models import Post
class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.json = b'{"name" : "example", "start_date" : "04/04/2022", "price" : 0}'
        self.post = Post(name="example", start_date="2022-04-04", price=0)

    def test_json_to_model(self):
        stream = io.BytesIO(self.json)
        serializer = PostSerializer(data=JSONParser().parse(stream))
        self.assertEqual(serializer.is_valid(), True)
        self.assertEqual(Post(**serializer.validated_data), self.post)
    
    def test_model_to_json(self):
        serializer = PostSerializer(instance=self.post)
        self.assertEqual(JSONRenderer().render(serializer.data), self.json)