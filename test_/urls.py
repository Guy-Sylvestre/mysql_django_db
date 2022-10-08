from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="project"),
    path('create-project/', views.createProject, name="create-project"),
    path('delete-project/', views.deleteProject, name="delete-project"),
]
