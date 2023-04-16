from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viewEmployee/<str:Eid>/', views.viewEmployee, name='viewEmployee'),
    path('addEmployee/', views.addEmployee, name='addNewEmployee'),
    path('updateEmployee/<str:Eid>/', views.updateEmployee, name='updateEmployee'),
    path('delete/<str:Eid>/', views.deleteEmployee, name='deleteEmployee'),
]