from django.urls import path
from . import views
from .views import home, expense, income, displayExpense, deleteExpense, registration, login_view, logout_view
urlpatterns=[
    path('home', home ,name='home'),
    path('expense', expense, name='expense'),
    path('income', income, name='income'),
    path('delete/<int:id>/', views.deleteExpense, name='deleteExpense'),
    path('displayexpense', displayExpense, name='displayexpense'),
    path('', registration, name='reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
]