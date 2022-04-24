from django.contrib import messages
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from loan.forms import AddLoanForm
from loan.models import Loan
# Create your views here.


class AddLoan(View):

    @method_decorator(login_required)
    def get(self, request):

        context = {
            'form' : AddLoanForm()
        }

        return render(request, 'loan/add_loan.html',context)

    @method_decorator(login_required)
    def post(self, request):

        form = AddLoanForm(request.POST)

        if form.is_valid():

            loan_data = form.save(commit=False)

            loan_data.user= request.user

            loan_data.save()

            messages.success(request, "Loan Data Added Successfully.")

            return redirect('add-loan')

        context = {
            'form': form
        }

        return render(request, 'loan/add_loan.html',context)


@login_required
def delete_loan(request, pk):
    loan_data = get_object_or_404(Loan,pk=pk,user=request.user)
    loan_data.delete()
    messages.info(request, "Loan data is deleted.")
    return redirect('homepage')



