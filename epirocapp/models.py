from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Create your models here.
class Employee(models.Model):
    emp_code = models.CharField(max_length=50)
    full_name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    courses = models.ForeignKey(Courses,on_delete=models.CASCADE)
    java = models.CharField(max_length=50)
    cplusplus = models.CharField(max_length=50)
    csharp = models.CharField(max_length=50)
    selenium = models.CharField(max_length=50)
    python = models.CharField(max_length=50)
    powerbi = models.CharField(max_length=50)
    azuredevops = models.CharField(max_length=50)
