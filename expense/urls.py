
from django.urls import path
from expense.views import AddExpenseView, delete_expense_view

urlpatterns = [
    path('add-expense',AddExpenseView.as_view(),name='add-expense'),
    path('delete-expense/<int:pk>',delete_expense_view,name='delete-transaction'),
]