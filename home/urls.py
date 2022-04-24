
from django.urls import path

from home.views import Home,current_balance

urlpatterns = [
    path('',Home.as_view(),name='homepage'),
    path('current-balance/',current_balance,name='current-balance'),
]