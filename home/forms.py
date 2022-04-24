
from django import forms
from datetime import datetime

type = (
        ('expense','expense'),
        ('loan','loan')
    )

class SearchForm(forms.Form):

    from_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    to_date= forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }),required=False)
    
    type = forms.ChoiceField(choices=type)


    def clean(self):
        cleaned_data = super().clean()

        from_date = cleaned_data.get('from_date')
        to_date= cleaned_data.get('to_date')

        if to_date and from_date > to_date:
            raise forms.ValidationError('From Date can\'t be higher than To Date.')
        elif from_date > datetime.now().date() or (to_date and to_date > datetime.now().date()):
            raise forms.ValidationError("Date can't be later than today.")

        return cleaned_data