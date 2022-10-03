from django.shortcuts import render

from django.http import HttpResponse

def tracker(request):
    return render(request, 'tracker.html')


def about(request):
    return render(request, 'about.html')



