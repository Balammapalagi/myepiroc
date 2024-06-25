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


def employee_form(request, id=0):
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
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/signin')


def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # print(username,email,pass1,pass2)
        if pass1 != pass2:
            return HttpResponse("your pass word didnt match")
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('signin')
        # return HttpResponse("User has been created successufuullly")
    return render(request, "epirocapp/signup.html", {})


def signin_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pawd')
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/employee_records')
        else:
            return HttpResponse("username or password incorrect")
    return render(request, "epirocapp/signin.html", {})


def logout_page(request):
    login(request)
    return redirect('logout')


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee_records')
    else:
        form = EmployeeForm()
    # return render(request, "epirocapp/employee_form.html", {'form': form})
    return render(request, "epirocapp/employee_form.html", {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, isinstance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, "epirocapp/employee_edit.html", {'employee': employee})


def delete(request):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')


def employee_delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')
