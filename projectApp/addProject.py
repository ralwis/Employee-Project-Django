from django.forms import ModelForm
from . models import employeeTable, projectTable, ProjectEmployeeTable

class addNewProject(ModelForm):
    class Meta():
        model = projectTable
        fields = '__all__'

class addNewProjectMembers(ModelForm):
    class Meta():
        model = ProjectEmployeeTable
        fields = '__all__'