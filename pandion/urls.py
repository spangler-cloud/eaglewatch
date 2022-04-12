from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get/ajax/selectbird', views.birdselectDB, name = "selectbird"),
    path('search', views.index, name = "search"),
    path('livestreams', views.livestreams, name = "livestreams"),
]
