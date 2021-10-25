import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, RegexValidator 
from django.db.models.functions import Now

class Post(models.Model):
    name = models.TextField(
        help_text='Product Name',
        validators=[MinLengthValidator(limit_value=4),
                    MaxLengthValidator(limit_value=10),
                    RegexValidator("[a-zA-Z0-9][a-zA-Z0-9\- ]{3,9}")],
        verbose_name='product name',
        primary_key=True
    )
    # json doesnt support dates
    # https://stackoverflow.com/questions/49882526/validation-for-datefield-so-it-doesnt-take-future-dates-in-django
    start_date = models.DateField(
        help_text='Product Positing Start Date',
        validators=[MinValueValidator(limit_value=datetime.date.today())],
        verbose_name='start date'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__gte=Now()),
                name='start_date_must_be_in_future'
            )
        ]

    price = models.IntegerField()