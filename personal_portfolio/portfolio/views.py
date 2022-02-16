from django.shortcuts import render
from portfolio import models


def home(request):
    projects = models.Project.objects.all()
    
    return render(request, 'portfolio/home.html', {'projects': projects})
