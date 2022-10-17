from django.db import models
from datetime import date

# Create your models here.
class Eagle(models.Model):
    name = models.CharField(max_length=1000, unique =  True)
    id = models.CharField(max_length=1000, unique =  True, primary_key=True)
    type = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=1000, unique =  True)
    id = models.CharField(max_length=1000, unique =  True, primary_key=True)
    region = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class TopLocations(models.Model):
    locName = models.CharField(max_length=1000, primary_key=True)
    howMany = models.IntegerField()

    def __str__(self):
        return self.locName

class TopStates(models.Model):
    state = models.CharField(max_length=1000, primary_key=True)
    howMany = models.IntegerField()

    def __str__(self):
        return self.state

class EagleScore(models.Model):
    state = models.CharField(max_length=1000, primary_key=True)
    eaglescore = models.IntegerField()

    def __str__(self):
        return self.state


class TopStateLocationTwo(models.Model):
    state = models.CharField(max_length=1000)
    locName = models.CharField(max_length=1000, primary_key=True)
    howMany = models.IntegerField()

    def __str__(self):
        return self.state


class Flag(models.Model):
    state = models.CharField(max_length=200)
    photo = models.ImageField()
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug