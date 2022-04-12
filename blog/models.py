from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    species = models.CharField(max_length=200)
    details = models.TextField(max_length=260)
    location = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    photo = models.ImageField()
    photo_Small = models.ImageField(default='default.jpg')
    camera = models.CharField(max_length=200, default="ILCE-1")
    lens = models.CharField(max_length=200, default="FE 600mm F4 GM")
    mm = models.CharField(max_length=200, default="600")
    aperture = models.CharField(max_length=200, default="f/4.0")
    shutter = models.CharField(max_length=200, default="1/3200")
    iso = models.CharField(max_length=200, default="400")
    ev = models.CharField(max_length=200, default="0.0")
    captured = models.DateTimeField(default=datetime.now, blank=True)
    captured_Date = models.DateField(default=datetime.now, blank=True)
    upload_Date = models.CharField(max_length=200, default=date.today)
    sequence = models.CharField(max_length=200, default="1")
    status = models.IntegerField(choices=STATUS, default=1)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.slug