
from django import forms
from django.forms import widgets
from loan.models import Loan
from datetime import datetime


class AddLoanForm(forms.ModelForm):

    class Meta:

        model = Loan

        fields = ['person','detail','type','loan_time','amount']

        widgets = {
            'loan_time': forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get('type')

        if not cleaned_data.get('loan_time') and (type == 'Loan Gave to' or type == 'Loan Gave by'):
            raise forms.ValidationError(message="Please Enter Loan Time.")
        elif cleaned_data.get('loan_time') and cleaned_data.get('loan_time') <= datetime.now().date():
            raise forms.ValidationError(message="Please Enter Valid Loan Time.")

        return cleaned_data

        