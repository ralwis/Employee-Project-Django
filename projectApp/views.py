from django.shortcuts import render, redirect
from . models import projectTable, ProjectEmployeeTable
from .addProject import addNewProject, addNewProjectMembers

def home(req):
    project = projectTable.objects.all()
    return render(req, "indexProject.html", {'projects':project})

def viewProject(req, Pid):
    viewproject = projectTable.objects.get(Pid = Pid)
    viewteam = ProjectEmployeeTable.objects.filter(Pid = Pid)
    return render(req, "viewProject.html", {'viewteam':viewteam, 'viewproject':viewproject,})

def addProject(req):
    addProject = addNewProject()
    if req.method == 'POST':
        addProject = addNewProject(req.POST)
        if addProject.is_valid():
            addProject.save()
            return redirect('projectHome')
    return render(req, ('addProject.html'), {'addProjects':addProject})

def addProjectMember(req, Pid):
    currentTeam = ProjectEmployeeTable.objects.get(Pid = Pid)
    updateTeam = addNewProjectMembers(instance=currentTeam)
    if req.method == "POST":
        updateTeam = addNewProjectMembers(req.POST, instance=currentTeam)
        if updateTeam.is_valid():
            updateTeam.save()
            return redirect('projectHome')
    return render(req, 'addTeam.html', {'addTeams':updateTeam})

def updateProject(req, Pid):
    currentProject = projectTable.objects.get(Pid = Pid)
    updateProject = addNewProject(instance=currentProject)
    if req.method == "POST":
        updateProject = addNewProject(req.POST, instance=currentProject)
        if updateProject.is_valid():
            updateProject.save()
            return redirect('projectHome')
    return render(req, 'addProject.html', {'addProjects':updateProject})

def deleteProject(req, Pid):
    currentProject = projectTable.objects.get(Pid = Pid)
    if req.method == "POST":
        currentProject.delete()
        return redirect('projectHome')
    return render(req, "deleteProject.html")
# Create your views here.
