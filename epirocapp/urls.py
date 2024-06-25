"""
URL configuration for myepiroc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup_page, name='signup'),
    path('signin/', views.signin_page, name='signin'),
    path('employee_records/', views.employee_list, name='employee_list'),# get all list or display all records
    path('employee_delete<int:id>/', views.employee_delete, name='employee_delete'),  # get all list or display all records
    path('edit/<int:id>/', views.edit, name='edit'), # get all list or display all recwords
    path('update/<int:id>', views.update), # get all list or display all records
]
