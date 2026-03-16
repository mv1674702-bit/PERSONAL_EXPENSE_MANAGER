from django.shortcuts import render, redirect
from petapp.models import Expense, Income
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense, Income
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
    return render(request,'login.html')

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return redirect('login')
    return render(request,'reg.html')

@login_required
def home(request):

    expenses = Expense.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)

    return render(request, 'home.html', {'expenses': expenses, 'incomes': incomes})

@login_required
def expense(request):
    if request.method == "POST":
        title = request.POST['title']
        amount = float(request.POST['amount'])
        category = request.POST['category']
        
        expense = Expense.objects.create(user=request.user, title=title, amount=amount, category=category)
        expense.save()

        return redirect('home')
    return render(request,'expense.html')

@login_required
def income(request):
    if request.method == "POST":
        source = request.POST['source']
        amount = request.POST['amount']
        
        income = Income(user=request.user, source=source, amount=amount)
        income.save()

        return redirect('home')
    return render(request,'income.html')

@login_required
def deleteExpense(request, id):
    expense = Expense.objects.get(pk=id, user=request.user)
    expense.delete()

    return redirect('home')

def logout_view(request):

    logout(request)
    
    return redirect('login')
