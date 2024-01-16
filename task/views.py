from django.shortcuts import render


tasklist = ['study', 'workout', 'cook','check mail']
# Create your views here.
def task_view (request):
    return render (request,'task/index.html',{
        'tasklist': tasklist
    } )

def add_task (request):
    return render (request, 'task/add.html')
