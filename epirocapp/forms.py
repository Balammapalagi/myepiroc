from  django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        fields = ('full_name', 'email', 'contact', 'emp_code','courses', 'java', 'cplusplus', 'csharp','selenium'
                  , 'python', 'powerbi', 'azuredevops')
        labels = {'full_name': 'full_name',
                  'email': 'email',
                  'contact': 'contact',
                  'emp_code': 'emp_code',
                  'courses': 'courses',
                  'java': 'java',
                  'cplusplus': 'cplusplus',
                  'csharp': 'csharp',
                  'selenium': 'selenium',
                  'python': 'python',
                  'powerbi': 'powerbi',
                  'azuredevops': 'azuredevops'
                  }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['courses'].empty_label = "select"
        self.fields['emp_code'].required = False
