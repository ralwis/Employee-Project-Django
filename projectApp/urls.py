from django.urls import path
from . import views

urlpatterns = [
    path('projectHome/', views.home, name='projectHome'),
    path('viewProject/<str:Pid>/', views.viewProject, name='viewProject'),
    path('addProject/', views.addProject, name='addNewProject'),
    path('updateProject/<str:Pid>/', views.updateProject, name='updateProject'),
    path('addTeam/<str:Pid>/', views.addProjectMember, name='addNewMember'),
    path('deleteProjevt/<str:Pid>/', views.deleteProject, name='deleteProject'),
]
