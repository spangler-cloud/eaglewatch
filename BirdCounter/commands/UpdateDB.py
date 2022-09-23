from pandion.models import Observation
from BirdCounter.models import Eagle
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from dotenv import load_dotenv
import os

load_dotenv()
eBIRD_KEY = os.getenv('eBIRD_KEY')

class Command(BaseCommand):
    def Update_DB(self, bird):
        headers =  {'X-eBirdApiToken' : eBIRD_KEY}
        locations = ('US-WA')
        i = 0
        for location in locations:
            print("API call for: " + location + ', ' + bird)
            api_url = "https://api.ebird.org/v2/data/obs/" + location + '/recent/' + bird + '?back=1'
            response = requests.get(api_url, headers=headers)
            hold = response.json()
            for spot in hold:
                try:
                    z = Observation(speciesCode = spot["speciesCode"], comName = spot["comName"], locId =  spot["locId"], locName =  spot["locName"], obsDt =  spot["obsDt"], lat = spot["lat"], lng = spot["lng"], howMany = spot[ "howMany"])
                    i += 1
                except KeyError as exception:
                    print('"How many" returned error, defaulting to 1')
                    z = Observation(speciesCode = spot["speciesCode"], comName = spot["comName"], locId =  spot["locId"], locName =  spot["locName"], obsDt =  spot["obsDt"], lat = spot["lat"], lng = spot["lng"], howMany = '1')
                    i += 1
                try:
                    z.save()
                except:
                    print('Duplicte or bad entry, skiping...')
                    continue

    def Bird_Gen(self):
        p = []
        for bird in Eagle.objects.all().values_list('id'):
            p.append(bird[0])

        for z in p:
            self.Update_DB(z)


    def handle(self, *args, **kwargs):
        self.Bird_Gen()
        print("Database Updated!")
