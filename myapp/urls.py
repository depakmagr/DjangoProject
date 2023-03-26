from django.urls import path
from .views import *    # relative import.


urlpatterns = [
    path("", index),
    path("template/", template),
    path("students/", students),
    # path("inside-template/", inside_template),
    path("<str:name>/", name_func),
    path("home", home),
]