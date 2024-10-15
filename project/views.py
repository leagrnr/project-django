from django.shortcuts import render, get_object_or_404
from project.models import Project

def show_descendants(request, project_name):
    project = get_object_or_404(Project, name=project_name)
    descendants = project.get_descendants()
    context = {'descendants': descendants}
    return render(request, 'show_descendants.html', context)