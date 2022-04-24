from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from home.forms import SearchForm
from expense.models import Transaction
from django.db.models import Q
from datetime import datetime, timedelta
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from loan.models import Loan


@login_required
def current_balance(request):
    all_transaction = Transaction.objects.filter(user=request.user)
    added = all_transaction.filter(type__iexact = 'Added').aggregate(added=Sum('amount'))['added']
    spent = all_transaction.filter(type__iexact = 'Spent').aggregate(spent=Sum('amount'))['spent']
    actual_balance = added - spent if added and spent else added if added else -spent if spent else "No Transaction"

    if actual_balance == "No Transaction":
        messages.info(request,"You have done no transaction.")
    elif int(actual_balance) > 0:
        messages.success(request,f"Your Current Balance is {actual_balance}")
    else:
        messages.warning(request,f"Be careful! Your amount is {actual_balance}")
        
    return redirect('homepage')

@login_required
def current_loan(request):
    loan_data = Loan.objects.filter(user= request.user)
    loan_paid_to = ''
    loan_paid_by = ''

    

class Home(View):

    @method_decorator(login_required)
    def get(self, request):

        form = SearchForm()
        context = {
            'form' : form,
        }

        return render(request,'home/homepage.html',context)

    @method_decorator(login_required)
    def post(self, request):

        form = SearchForm(request.POST)

        if form.is_valid():

            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']

            type = form.cleaned_data['type']

            if type == 'expense':

                if not to_date:

                    transaction_data =Transaction.objects.filter(
                            Q(date__gte = from_date)&Q(date__lte = (datetime.now().date() + timedelta(days=15))),
                            user=request.user
                            )
                else:
                    transaction_data =Transaction.objects.filter(
                            Q(date__gte = from_date)&Q(date__lte = to_date),
                            user=request.user
                            )

                total_added = transaction_data.filter(type = 'Added').aggregate(total_added=Sum('amount'))['total_added']
                total_spent = transaction_data.filter(type = 'Spent').aggregate(total_added=Sum('amount'))['total_added']

                context = {
                    'data' : transaction_data,
                    'form' : form,
                    'total_added' : total_added,
                    'total_spent' : total_spent,
                    'actual_balance' : total_added - total_spent if total_added and total_spent else total_added if total_added else -total_spent

                }
                
                return render(request, 'home/homepage.html',context)

            else:
                if not to_date:
                    loan_data = Loan.objects.filter(
                        Q(date__gte = from_date)&Q(date__lte = (datetime.now().date() + timedelta(days=15))),
                            user=request.user
                    )
                else:
                    loan_data = Loan.objects.filter(
                            Q(date__gte = from_date)&Q(date__lte = to_date),
                            user=request.user
                            )
                
                loan_paid_by = loan_data.filter(type__iexact='Loan Paid by').aggregate(paid_by=Sum('amount'))['paid_by']
                loan_paid_to = loan_data.filter(type__iexact='Loan Paid to').aggregate(paid_to=Sum('amount'))['paid_to']
                loan_gave_to = loan_data.filter(type__iexact='Loan Gave to').aggregate(gave_to=Sum('amount'))['gave_to']
                loan_gave_by = loan_data.filter(type__iexact='Loan Gave by').aggregate(gave_by=Sum('amount'))['gave_by']

                context = {
                    'loan_data': loan_data,
                    'form':form,
                    'paid_by':loan_paid_by,
                    'paid_to':loan_paid_to,
                    'gave_by':loan_gave_by,
                    'gave_to':loan_gave_to
                }

                return render(request, 'home/homepage.html',context)

        context = {
            'form':form
        }

        return render(request,'home/homepage.html',context)



