from django.db import models
from datetime import date

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100, unique =  True)
    id = models.CharField(max_length=100, unique =  True, primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Observation(models.Model):
    speciesCode = models.CharField(max_length=100)
    comName = models.CharField(max_length=100)
    locId = models.CharField(max_length=100)
    locName = models.CharField(max_length=100)
    obsDt = models.CharField(max_length=100)
    howMany = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    mod_date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['speciesCode', 'obsDt', 'locId'], name='no_duplicate_obs')
            ]

    def __str__(self):
        return self.comName + ': ' + self.obsDt

class Notable(models.Model):
    speciesCode = models.CharField(max_length=100)
    comName = models.CharField(max_length=100)
    locId = models.CharField(max_length=100)
    locName = models.CharField(max_length=100)
    obsDt = models.CharField(max_length=100)
    howMany = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    mod_date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['speciesCode', 'obsDt', 'locId'], name='no_duplicate__notable_obs')
            ]

    def __str__(self):
        return self.comName + ': ' + self.obsDt
