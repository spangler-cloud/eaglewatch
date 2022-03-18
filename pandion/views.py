from django.shortcuts import render
from django.http import JsonResponse
from . import search
from . import recent_list
from .models import Bird
from .models import Notable
import requests
import json
from dotenv import load_dotenv
import os

def index(request):
    rapters = Bird.objects.filter(type="Rapter").values_list('id', 'name')
    owls = Bird.objects.filter(type="Owl").values_list('id', 'name')
    passeriformes = Bird.objects.filter(type="Passeriformes").values_list('id', 'name')
    waterfowl = Bird.objects.filter(type="Waterfowl").values_list('id', 'name')
    recentlist = recent_list.ListFunction()
    load_dotenv()
    Google_Maps_Key = os.getenv('Google_Maps_Key')
    return render(request, 'search.html',{'rapters':rapters, "owls":owls, "passeriformes":passeriformes, "waterfowl":waterfowl, "Google_Maps_Key":Google_Maps_Key, "recentlist":recentlist })

def birdselectDB(request):
    return JsonResponse(search.SearchFunction(request), status=200, safe=False)

def photos(request):
    return render(request, 'photos.html')

def about(request):
    return render(request, 'about.html')

def test(request):
    return render(request, 'test.html')
