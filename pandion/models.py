from django.db import models
from datetime import date

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=1000, unique =  True)
    id = models.CharField(max_length=1000, unique =  True, primary_key=True)
    type = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Observation(models.Model):
    speciesCode = models.CharField(max_length=1000)
    comName = models.CharField(max_length=1000)
    locId = models.CharField(max_length=1000)
    locName = models.CharField(max_length=1000)
    obsDt = models.CharField(max_length=1000)
    howMany = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    lng = models.CharField(max_length=1000)
    mod_date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['speciesCode', 'obsDt', 'locId'], name='no_duplicate_obs')
            ]

    def __str__(self):
        return self.comName + ': ' + self.obsDt

class Notable(models.Model):
    speciesCode = models.CharField(max_length=1000)
    comName = models.CharField(max_length=1000)
    locId = models.CharField(max_length=1000)
    locName = models.CharField(max_length=1000)
    obsDt = models.CharField(max_length=1000)
    howMany = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    lng = models.CharField(max_length=1000)
    mod_date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['speciesCode', 'obsDt', 'locId'], name='no_duplicate__notable_obs')
            ]

    def __str__(self):
        return self.comName + ': ' + self.obsDt
