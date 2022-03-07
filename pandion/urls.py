from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get/ajax/selectbird', views.birdselectDB, name = "selectbird"),
    path('search', views.index, name = "search"),
    path('photos', views.photos, name = "photos"),
    path('about', views.about, name = "about"),
    path('test', views.test, name = "test"),
]
