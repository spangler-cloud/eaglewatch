from pandion.models import Observation
from BirdCounter.models import Eagle
from BirdCounter.models import State
import requests
import json
from django.core.management.base import BaseCommand, CommandError
from dotenv import load_dotenv
import os
from pandion.toplocations import AddTotal

load_dotenv()
eBIRD_KEY = os.getenv('eBIRD_KEY')

class Command(BaseCommand):
    def Update_DB(self, states):
        headers =  {'X-eBirdApiToken' : eBIRD_KEY}
        bird = "baleag"
        i = 0
        for state in states:
            print("API call for: " + state + ', ' + bird)
            api_url = "https://api.ebird.org/v2/data/obs/" + state + '/recent/' + bird + '?back=1'
            response = requests.get(api_url, headers=headers)
            hold = response.json()
            for spot in hold:
                try:
                    z = Observation(speciesCode = spot["speciesCode"], comName = spot["comName"], locId =  spot["locId"], locName =  spot["locName"], obsDt =  spot["obsDt"], lat = spot["lat"], lng = spot["lng"], howMany = spot[ "howMany"], state = state)
                    i += 1
                except KeyError as exception:
                    print('"How many" returned error, defaulting to 1')
                    z = Observation(speciesCode = spot["speciesCode"], comName = spot["comName"], locId =  spot["locId"], locName =  spot["locName"], obsDt =  spot["obsDt"], lat = spot["lat"], lng = spot["lng"], howMany = '1', state = state)
                    i += 1
                try:
                    z.save()
                    try:
                        AddTotal(spot["locId"], spot["locName"], spot[ "howMany"], state )
                    except:
                        AddTotal(spot["locId"], spot["locName"], "1", state )
                except:
                    print('Duplicte or bad entry, skiping...')
                    continue


    def State_Gen(self):
        states = []
        for state in State.objects.filter(region="Midwest").values_list('id'):
            states.append(state[0])

        self.Update_DB(states)


    def handle(self, *args, **kwargs):
        self.State_Gen()
        print("Database Updated!")