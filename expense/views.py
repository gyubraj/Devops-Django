from django.shortcuts import redirect, render
from django.views import View
from expense.forms import AddExpenseForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

from expense.models import Transaction
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

class AddExpenseView(View):

    @method_decorator(login_required)
    def get(self, request):

        context = {
            'form' : AddExpenseForm()
        }

        return render(request, 'expense/add_expense.html',context)

    @method_decorator(login_required)
    def post(self, request):

        form = AddExpenseForm(request.POST)

        if form.is_valid():
            expense_save = form.save(commit=False)
            expense_save.user = request.user
            expense_save.save()
            messages.info(request,"Your Transaction added successfully.")

            return redirect('add-expense')
        
        context = {
            'form' : form
        }

        return render(request, 'expense/add_expense.html',context)


@login_required
def delete_expense_view(request, pk):
    expense = get_object_or_404(Transaction, pk = pk, user=request.user)

    expense.delete()

    messages.success(request, message="Transaction is deleted.")

    return redirect('homepage')

    



