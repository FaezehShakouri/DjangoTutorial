from http.client import ImproperConnectionState
from operator import le
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    
    if request.GET.get('special'):
        characters.extend('~!@#$%^&*()_')
    
    lenght = int(request.GET.get('lenght'))

    thepassword = ''
    for i in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')