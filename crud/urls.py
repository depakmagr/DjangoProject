from django.urls import path
from .views import *    # relative import.


urlpatterns = [
    path("", home, name=home),
]
