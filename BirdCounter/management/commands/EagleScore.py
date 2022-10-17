from pandion.models import Observation
from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from BirdCounter.models import EagleScore

class Command(BaseCommand):
    def top(self):
        EagleScore.objects.all().delete()
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

        state_pop = {
            'AK': 738023,
            'AL': 5073187,
            'AR': 3030646,
            'AZ': 7303398,
            'CA': 39995077,
            'CO': 5922618,
            'CT': 3612314,
            'DC': 701974,
            'DE': 1008350,
            'FL': 22085563,
            'GA': 10916760,
            'HI': 1474265,
            'IA': 3219171,
            'ID': 1893410,
            'IL': 12808884,
            'IN': 6845874,
            'KS': 2954832,
            'KY': 4539130,
            'LA': 4682633,
            'MA': 7126375,
            'MD': 6257958,
            'ME': 1369159,
            'MI': 10116069,
            'MN': 5787008,
            'MO': 6188111,
            'MS': 2960075,
            'MT': 1103187,
            'NC': 10620168,
            'ND': 800394,
            'NE': 1988536,
            'NH': 1389741,
            'NJ': 9388414,
            'NM': 2129190,
            'NV': 3185426,
            'NY': 20365879,
            'OH': 11852036,
            'OK': 4000953,
            'OR': 4318492,
            'PA': 13062764,
            'RI': 1106341,
            'SC': 5217037,
            'SD': 901165,
            'TN': 7023788,
            'TX': 29945493,
            'UT': 3373162,
            'VA': 8757467,
            'VT': 646545,
            'WA': 7901429,
            'WI': 5935064,
            'WV': 1781860,
            'WY': 579495
                    }
        for obs in Observation.objects.filter(obsDt__range=[timezone.now().date() - timedelta(days=14), timezone.now().date()]).values():
            if obs["state"][3:] in d:
                d[obs["state"][3:]]  += int(obs["howMany"])
            else:
                d[obs["state"][3:]]  = int(obs["howMany"])

        for key, value in d.items():
            t.update({state_names[key]:(d[key]/state_pop[key])*100000})


        sorted_dt = {key: value for key, value in sorted(t.items(), key=lambda item: item[1], reverse=True)}

        l = []
        for x in sorted_dt:
            q = EagleScore(state = x, eaglescore =  sorted_dt[x])
            q.save()


    def handle(self, *args, **kwargs):
        self.top()