from django.db import models
import uuid
from django.core.validators import RegexValidator

# Create your models here.

class employeeTable(models.Model):
    Eid = models.AutoField(primary_key=True)
    firstName = models.CharField(default='', max_length=50)
    lastName = models.CharField(default='', max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], default='')
    designation = models.CharField(default='', max_length=50)
    
    def __str__(self):
        return str(self.Eid) + " - "+ self.firstName +" " + " "+ self.lastName +" "
    
    
# class projectTable(models.Model):
#     Pid = models.AutoField(primary_key=True)
#     projectName = models.CharField(max_length=50)
#     startedDate = models.DateField(null=True)
#     description = models.TextField()
#     leader = models.ForeignKey(employeeTable,default='', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return str(self.Pid) + " - "+ self.projectName +" "
    
    
# class ProjectEmployeeTable(models.Model):
#     project = models.OneToOneField(projectTable,unique=True, on_delete=models.CASCADE)
#     employee = models.ManyToManyField(employeeTable)
    
#     def __str__(self):
#         return str(self.project)