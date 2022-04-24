from django.forms import ModelForm
from expense.models import Transaction


class AddExpenseForm(ModelForm):

    class Meta:

        model = Transaction
        fields = ['title','description','type','amount']
        

