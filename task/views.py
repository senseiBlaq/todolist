from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm (forms.Form):
        task = forms.CharField(
            label = 'New Activiy',
            widget=forms.TextInput(attrs={'placeholder': 'Add an activity'})
        )

# Create your views here.
def task_view (request):
    if 'tasklist' not in request.session:
        request.session['tasklist'] = []
    return render (request,'task/index.html',{
        'tasklist': request.session ['tasklist']
    } )

def add_task (request):
    # check if the methaod is a post (state altering)
    if request.method == 'POST':
        form = NewTaskForm(request.POST) # store user input in this class instancer
        #check the user input is the correct on the server side
        if form.is_valid():
            task = form.cleaned_data ['task'] #extracts validated and cleaned data from the input field task(in the class) into the variable
            request.session['tasklist'] += [task] #adds to list of activiities in the session
            return HttpResponseRedirect(reverse("task:task_view")) #takes the user back to the task list
        else:
            return render (request, 'task/add.html', {
                'form': form
            })

    return render (request, 'task/add.html', {
        'form': NewTaskForm()
    })
