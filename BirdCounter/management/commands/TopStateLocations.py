from pandion.models import Observation
from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from BirdCounter.models import TopStateLocationTwo
from BirdCounter.models import State

class Command(BaseCommand):
    def top(self, state):
        TopStateLocationTwo.objects.filter(state=state).delete()
        d = {}
        print("working on " + state)
        for obs in Observation.objects.filter(obsDt__range=[timezone.now().date() - timedelta(days=14), timezone.now().date()], state=state).values():
            if obs["locName"] in d:
                d[obs["locName"]] += int(obs["howMany"])
            else:
                d[obs["locName"]] = int(obs["howMany"])


        sorted_dt = {key: value for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True)}

        l = []
        n = 0
        for x in sorted_dt:
            q = TopStateLocationTwo(state=state[3:].lower(), locName = x, howMany =  sorted_dt[x])
            q.save()
            if n > 25:
                break
            n += 1


    def State_Gen(self):
        for state in State.objects.values_list('id'):
            self.top(state[0])



    def handle(self, *args, **kwargs):
        self.State_Gen()