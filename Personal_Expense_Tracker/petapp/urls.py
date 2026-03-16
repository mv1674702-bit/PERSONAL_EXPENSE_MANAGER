from django.urls import path
from petapp.views import home, login_view, registration, expense, income, deleteExpense, logout_view
urlpatterns=[
    path('home', home ,name='home'),
    path('expense', expense, name='expense'),
    path('income', income, name='income'),
    path('delete/<int:id>', deleteExpense, name='delete'),
    path('', registration, name='reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]