from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('test1', views.test1),
    path('test2', views.test2),
]