from django.shortcuts import render, redirect
from . models import employeeTable
from .addEmployee import addNewEmployee

def home(req):
    employee = employeeTable.objects.all()
    return render(req, "index.html", {'employees':employee})

def viewEmployee(req, Eid):
    viewemployee = employeeTable.objects.get(Eid = Eid)
    return render(req, "viewEmployee.html", {'viewemployees':viewemployee})

def addEmployee(req):
    addEmployee = addNewEmployee()
    if req.method == 'POST':
        addEmployee = addNewEmployee(req.POST)
        if addEmployee.is_valid():
            addEmployee.save()
            return redirect('home')
    return render(req, ('addEmployee.html'), {'addEmployees':addEmployee})

def updateEmployee(req, Eid):
    currentEmployee = employeeTable.objects.get(Eid = Eid)
    updateEmployee = addNewEmployee(instance=currentEmployee)
    if req.method == "POST":
        updateEmployee = addNewEmployee(req.POST, instance=currentEmployee)
        if updateEmployee.is_valid():
            updateEmployee.save()
            return redirect('home')
    return render(req, 'addEmployee.html', {'addEmployees':updateEmployee})
    
def deleteEmployee(req, Eid):
    currentEmployee = employeeTable.objects.get(Eid = Eid)
    if req.method == "POST":
        currentEmployee.delete()
        return redirect('home')
    return render(req, "deleteEmployee.html")

def addProject(req, Pid):
    return render(req, "addProject.html")
# Create your views here.
