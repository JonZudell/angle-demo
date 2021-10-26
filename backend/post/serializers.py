from collections import OrderedDict
from rest_framework import serializers
from .models import Post
class PostListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return {"posts" : [super().to_representation(data)]}

    def to_internal_value(self, data):
        return super().to_internal_value(data['posts'])

class PostSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/48444665/django-rest-framework-datefield-format
    start_date = serializers.DateField(format="%m/%d/%Y", input_formats=["%m/%d/%Y"])
    class Meta:
        model = Post
        fields = ['name', 'start_date', 'price']
        list_serializer_class = PostListSerializer