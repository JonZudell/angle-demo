import datetime

from collections import OrderedDict
from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/48444665/django-rest-framework-datefield-format
    start_date = serializers.DateField(format="%m/%d/%Y", 
        input_formats=["%m/%d/%Y"],
        validators=[MinValueValidator(limit_value=datetime.date.today)])
    class Meta:
        model = Post
        fields = ['name', 'start_date', 'price']