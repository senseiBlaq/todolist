from django.shortcuts import render
from datetime import datetime


# Create your views here.
def isChristmas (request):
    now = datetime.now()
    return render (request, 'isholiday/index.html', {
        'christmas' : now.month == 12 and now.year == 25
    })

def time_day (request):
    now = datetime.now()
    return render (request, 'isholiday/index.html', {
        'hour': now.hour, 'minute': now.minute
    })

