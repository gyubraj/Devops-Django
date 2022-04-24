from django.urls import path
from loan.views import AddLoan,delete_loan

urlpatterns = [
    path('add-loan/',AddLoan.as_view(),name='add-loan'),
    path('delete-loan/<int:pk>',delete_loan,name='delete-loan'),
]