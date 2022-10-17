from django.shortcuts import render

from django.http import HttpResponse
from BirdCounter.models import TopLocations
from BirdCounter.models import TopStates
from django.utils import timezone
from datetime import date
from datetime import timedelta
from BirdCounter.models import TopStateLocationTwo
from BirdCounter.models import State
from BirdCounter.models import EagleScore
from BirdCounter.models import Flag
from django.views import generic


def toplocations(request):
    top = TopLocations.objects.values_list("locName", "howMany").order_by('howMany').reverse()
    date_since = timezone.now().date() - timedelta(days=14)
    df = date_since.strftime("%m/%d/%y")
    today = date.today()
    td = today.strftime("%m/%d/%y")
    topstates = TopStates.objects.values_list("state", "howMany").order_by('howMany').reverse()
    return render(request, 'toplocations.html', {"topstates": topstates, "top": top, "df": df, "td": td})

def topstates(request):
    date_since = timezone.now().date() - timedelta(days=14)
    df = date_since.strftime("%m/%d/%y")
    today = date.today()
    td = today.strftime("%m/%d/%y")
    topstates = TopStates.objects.values_list("state", "howMany").order_by('howMany').reverse()
    return render(request, 'topstates.html', {"topstates": topstates, "df": df, "td": td})

def eaglescore(request):
    date_since = timezone.now().date() - timedelta(days=14)
    df = date_since.strftime("%m/%d/%y")
    today = date.today()
    td = today.strftime("%m/%d/%y")
    eaglescore = EagleScore.objects.values_list("state", "eaglescore").order_by('eaglescore').reverse()
    return render(request, 'eaglescore.html', {"eaglescore": eaglescore, "df": df, "td": td})

def topstatelocations(request, state):
    print(state)
    date_since = timezone.now().date() - timedelta(days=14)
    df = date_since.strftime("%m/%d/%y")
    today = date.today()
    td = today.strftime("%m/%d/%y")
    topstatelocations = TopStateLocationTwo.objects.filter(state=state).values_list("locName", "howMany").order_by('howMany').reverse()
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
    state = state_names[state.upper()]
    return render(request, 'topstatelocations.html', {"topstatelocations": topstatelocations, "df": df, "td": td, "state": state})

def tracker(request):
    d = {}
    for x in State.objects.values_list('id', "name").order_by('name'):
        d[x[0][3:].lower()] = [x[1], 'https://pandion-photos.s3.amazonaws.com/media/' + x[0][3:].lower() + ".png"]
    p = {}
    q = Flag.objects.all()
    for s in q:
        p[s.state] = s.photo.url
    return render(request, 'tracker.html', {"d":d, "p":p})


def about(request):
    return render(request, 'about.html')

