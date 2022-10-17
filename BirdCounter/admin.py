from django.contrib import admin

from .models import Eagle
from .models import State
from .models import TopLocations
from .models import TopStates
from .models import TopStateLocationTwo
from .models import Flag

admin.site.register(Eagle)
admin.site.register(State)
admin.site.register(TopLocations)
admin.site.register(TopStates)
admin.site.register(TopStateLocationTwo)
admin.site.register(Flag)