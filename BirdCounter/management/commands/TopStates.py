from pandion.models import Observation
from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from BirdCounter.models import TopStates

class Command(BaseCommand):
    def top(self):
        TopStates.objects.all().delete()
        d = {}
        t = {}

        state_names = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
                        }
        for obs in Observation.objects.filter(obsDt__range=[timezone.now().date() - timedelta(days=14), timezone.now().date()]).values():
            if obs["state"][3:] in d:
                d[obs["state"][3:]]  += int(obs["howMany"])
            else:
                d[obs["state"][3:]]  = int(obs["howMany"])

        for key, value in d.items():
            t.update({state_names[key]:d[key]})

        sorted_dt = {key: value for key, value in sorted(t.items(), key=lambda item: item[1], reverse=True)}

        l = []
        for x in sorted_dt:
            q = TopStates(state = x, howMany =  sorted_dt[x])
            q.save()


    def handle(self, *args, **kwargs):
        self.top()