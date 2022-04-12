from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='photos'),
    path('photos', views.PostList.as_view(), name='photos'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]