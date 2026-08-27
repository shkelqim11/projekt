from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sherbimet/", views.sherbimet, name="sherbimet"),
    path("rreth-nesh/", views.rreth_nesh, name="rreth-nesh"),
]