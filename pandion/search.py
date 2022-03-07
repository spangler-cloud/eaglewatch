import requests
import json
from .models import Observation
from .models import Notable

def SearchFunction(request):
    c = request.POST
    bird = c.get('selectbird')
    observations = []
    if bird == 'days':
        for x in Notable.objects.filter().values():
            observation = {'lat': float(x['lat']), 'lng': float(x['lng'])}, x['locName'], x["obsDt"], x["comName"]
            observations.append(observation)
    else:
        for x in Observation.objects.filter(speciesCode__contains=bird).values():
            observation = {'lat': float(x['lat']), 'lng': float(x['lng'])}, x['locName'], x["obsDt"], x["comName"]
            observations.append(observation)
    return observations
