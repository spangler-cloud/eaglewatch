from django.shortcuts import render
from django.http import JsonResponse
from . import search
from . import recent_list
from .models import Bird
from .models import Notable
from BirdCounter.models import State
import requests
import json
from dotenv import load_dotenv
import os

def index(request):
    south = State.objects.filter(region="South").values_list('id', 'name')
    west = State.objects.filter(region="West").values_list('id', 'name')
    midwest = State.objects.filter(region="Midwest").values_list('id', 'name')
    northeast = State.objects.filter(region="Northeast").values_list('id', 'name')
    recentlist = recent_list.ListFunction()
    load_dotenv()
    Google_Maps_Key = os.getenv('Google_Maps_Key')
    return render(request, 'search.html',{"south":south, "west":west, "midwest":midwest, "northeast": northeast, "Google_Maps_Key":Google_Maps_Key, "recentlist":recentlist })

def birdselectDB(request):
    return JsonResponse(search.SearchFunction(request), status=200, safe=False)

def photos(request):
    return render(request, 'photos.html')

def livestreams(request):
    return render(request, 'livestreams.html')

def home(request):
    return render(request, 'home.html')