from django.forms import ModelForm
from . models import employeeTable

class addNewEmployee(ModelForm):
    class Meta():
        model = employeeTable
        fields = '__all__'