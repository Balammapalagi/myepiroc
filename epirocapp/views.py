from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from .models import Employee

x = datetime.now()
y = x.strftime('%d-%m-%y')


# Create your views here.

@login_required(login_url='login')
def home_page(request):
    return render(request, "epirocapp/home.html", {})


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "epirocapp/employee_list.html", context)


def signup_page(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "epirocapp/signup.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/employee_list')


def signin_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pawd')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            return HttpResponse("username or password incorrect")
    return render(request, "epirocapp/signin.html", {})


def employee_delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee_list')

