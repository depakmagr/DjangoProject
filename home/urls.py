from django.urls import path
from .views import *    # relative import.


urlpatterns = [
    path("about/", about, name='about'),
    path("", index, name='index'),
    path("template/", template, name='template'),
    path("students/", students, name='students'),
    path("<str:name>/", name_func),
    path("home", home, name='home'),
]