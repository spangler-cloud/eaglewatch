from django.db import models
from datetime import date

# Create your models here.
class Eagle(models.Model):
    name = models.CharField(max_length=1000, unique =  True)
    id = models.CharField(max_length=1000, unique =  True, primary_key=True)
    type = models.CharField(max_length=1000)

    def __str__(self):
        return self.name