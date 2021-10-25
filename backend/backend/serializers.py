from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%m-%d-%Y")
    class Meta:
        model = Post
        fields = ['name', 'start_date', 'price']