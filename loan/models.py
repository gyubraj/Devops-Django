from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator

class Loan(models.Model):

    type_choices = (
        ('Loan Paid to','Loan Paid to'),
        ('Loan Paid by','Loan Paid by'),
        ('Loan Gave to','Loan Gave to'),
        ('Loan Gave by','Loan Gave by')

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    person = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=20,choices=type_choices)
    date = models.DateField(default=datetime.now().date())
    loan_time = models.DateField(null=True, blank=True)
    amount = models.IntegerField(validators=[MinValueValidator(limit_value=10,message="Can't store less than 10.")])

    def __str__(self) -> str:
        return f"{self.person} ---> {self.user.username}"

    
