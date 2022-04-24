from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime

from django.utils import timezone


class Transaction(models.Model):
    type_choices = (
        ('Added','Added'),
        ('Spent','Spent')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=6,choices=type_choices)
    amount = models.IntegerField(validators=[MinValueValidator(limit_value=5,message="You can't store less than 5 rupee.")])
    date = models.DateField(default=datetime.now().date())

    def __str__(self) -> str:
        return f'{self.user.username} --> {self.title}'

