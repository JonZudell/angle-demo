from django.db import models

class Post(models.Model):
    name = models.TextField(primary_key=True)
    start_date = models.DateField() 
    price = models.IntegerField()
    # will enforce start_date constraint in view
    #def clean(self):