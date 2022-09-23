from django.urls import path

from . import views

urlpatterns = [
    path('eaglewatch', views.index, name='index'),
]