import requests
import json
from .models import Observation
from .models import Notable
from .models import Bird
from BirdCounter.models import State
from datetime import timedelta
from django.utils import timezone

def SearchFunction(request):

    '''
    Takes desired species as input and returns all observations of that species over the last 14 days.
    '''

    c = request.POST
    bird = c.get('selectbird')
    observations = []
    if bird in [''.join(y) for y in State.objects.filter().values_list('id')]:
        for x in Observation.objects.filter(state__contains=bird, obsDt__range=[timezone.now().date() - timedelta(days=14), timezone.now().date()]).values():
            observation = {'lat': float(x['lat']), 'lng': float(x['lng'])}, x['locName'], x["obsDt"], x["comName"]
            observations.append(observation)
    return observations