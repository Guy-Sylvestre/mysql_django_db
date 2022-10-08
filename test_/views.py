from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProjectForm
# Create your views here.


def projects(request):
    project = Project.objects.all()

    context = {
        'projects': project,
    }

    return render(request, 'test_/index.html', context)


def createProject(request):
    """
        Creer un projet avec une image
    """
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()

            messages.success(request, f"{project} was created succefully!")
            return redirect('project')

    context = {
        "form": form
    }

    return render (request, 'test_/create-project.html', context)


def deleteProject(request, pk):
    
    project = Project.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f"{project} was deleted succefully!")
        return redirect('project')

    context = {
        "object": project,
    }

    return render(request, 'test_/delete-project.html', context)