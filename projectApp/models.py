from django.db import models
from employeeApp.models import employeeTable

# Create your models here.

class projectTable(models.Model):
    Pid = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=50)
    startedDate = models.DateField(null=True)
    description = models.TextField()
    leader = models.ForeignKey(employeeTable,default='', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Pid)
    
    
class ProjectEmployeeTable(models.Model):
    Pid = models.ForeignKey(projectTable, null=True, on_delete=models.CASCADE)
    employee = models.ManyToManyField(employeeTable, null=True)
    
    def __str__(self):
        return ', '.join([str(a) for a in self.employee.all()])
        # return str(self.employee)