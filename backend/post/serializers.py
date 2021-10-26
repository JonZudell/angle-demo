from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/48444665/django-rest-framework-datefield-format
    start_date = serializers.DateField(format="%m/%d/%Y", input_formats=["%m/%d/%Y"])
    class Meta:
        model = Post
        fields = ['name', 'start_date', 'price']