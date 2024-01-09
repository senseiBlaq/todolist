from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return render (request, 'playground/index.html')

def greeting (request, name):
    return render (request, 'playground/index.html', {
        'name': name.capitalize()
    })