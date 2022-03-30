import requests
import json
from .models import Observation
from .models import Notable
from .models import Bird

def SearchFunction(request):
    c = request.POST
    bird = c.get('selectbird')
    observations = []
    if bird in [''.join(y) for y in Notable.objects.filter().values_list("speciesCode").order_by('-id')[:20:-1] ]:
        for x in Notable.objects.filter(speciesCode__contains=bird).values():
            observation = {'lat': float(x['lat']), 'lng': float(x['lng'])}, x['locName'], x["obsDt"], x["comName"]
            observations.append(observation)
    if bird in [''.join(y) for y in Bird.objects.filter().values_list('id')]:
        for x in Observation.objects.filter(speciesCode__contains=bird).values():
            observation = {'lat': float(x['lat']), 'lng': float(x['lng'])}, x['locName'], x["obsDt"], x["comName"]
            observations.append(observation)
    return observations
