import io
from collections import OrderedDict
from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers import PostSerializer
from ..models import Post

#class PostListSerializerTestCase(TestCase):
#    def setUp(self):
#        self.json = b'{"post":[{"name":"example","start_date":"04/04/2022","price":0}]}'
#        self.posts = [Post(name="example", start_date="04/04/2022", price=0)]
#
#    def test_json_to_model(self):
#        stream = io.BytesIO(self.json)
#        serializer = PostSerializer(data=JSONParser().parse(stream), many=True)
#        self.assertEqual(serializer.is_valid(), True)
#        self.assertEqual(serializer.validated_data, self.posts)
#    
#    def test_model_to_json(self):
#        serializer = PostSerializer(instance=self.posts, many=True)
#        self.assertEqual(JSONRenderer().render(serializer.data), self.json)

class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.json = b'{"name":"example","start_date":"04/04/2022","price":0}'
        self.serializer = PostSerializer(data={"name" : "example", "start_date" : "04/04/2022", "price" : 0})
        self.post = Post(**self.serializer.validated_data)

    def test_json_to_model(self):
        stream = io.BytesIO(self.json)
        srl = PostSerializer(data=JSONParser().parse(stream))
        self.assertEqual(srl.is_valid(), True)
        self.assertEqual(Post(**srl.validated_data), self.post)
    
    def test_model_to_json(self):
        srl = PostSerializer(instance=self.post)
        self.assertEqual(JSONRenderer().render(srl.data), self.json)