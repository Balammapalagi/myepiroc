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
    path('signin/', views.signin_page, name='signin'),
    path('home/', views.home_page, name='home'),
    path('', views.signup_page, name='employee_insert'),
    path('employee_list<int:id>/', views.signup_page, name='employee_update'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_delete<int:id>/', views.employee_delete, name='employee_delete')
]
