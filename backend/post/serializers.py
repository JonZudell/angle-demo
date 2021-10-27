import datetime

from collections import OrderedDict
from rest_framework import serializers
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, RegexValidator 
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[MinLengthValidator(limit_value=4),
                    MaxLengthValidator(limit_value=10),
                    RegexValidator("[a-zA-Z0-9][a-zA-Z0-9\- ]{3,9}")])

    # https://stackoverflow.com/questions/48444665/django-rest-framework-datefield-format
    start_date = serializers.DateField(format="%m/%d/%Y", 
        input_formats=["%m/%d/%Y"],
        validators=[MinValueValidator(limit_value=datetime.date.today)])
        
    class Meta:
        model = Post
        fields = ['name', 'start_date', 'price']