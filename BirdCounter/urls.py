from django.urls import path

from . import views

urlpatterns = [
    path('tracker', views.tracker, name = "tracker"),
    path('about', views.about, name = "about"),
]