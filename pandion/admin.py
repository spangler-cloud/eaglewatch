from django.contrib import admin

# Register your models here.
from .models import Bird
from .models import Observation
from .models import Notable

admin.site.register(Bird)
admin.site.register(Observation)
admin.site.register(Notable)
