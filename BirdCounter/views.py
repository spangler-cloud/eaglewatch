from django.shortcuts import render

from django.http import HttpResponse

def eaglewatch(request):
    return render(request, 'eaglewatch.html')
