from django.urls import path

from . import views

urlpatterns = [
    path('', views.tracker, name = "tracker"),
    path('tracker', views.tracker, name = "tracker"),
    path('topstates', views.topstates, name = "topstates"),
    path('eaglescore', views.eaglescore, name = "eaglescore"),
    path('toplocations', views.toplocations, name = "toplocations"),
    path('topstatelocations/<str:state>/', views.topstatelocations, name = "topstatelocations"),
    path('about', views.about, name = "about"),
]


