from django.contrib import admin

from .models import Eagle
from .models import State

admin.site.register(Eagle)
admin.site.register(State)