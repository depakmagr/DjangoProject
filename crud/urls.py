from django.urls import path
from .views import *    # relative import.


urlpatterns = [
    path("home/", home, name='home'),
    path("create/", create, name="create"),
    path("classroom/", classroom, name="classroom"),
    path("file-test/", file_test, name="file_test"),
    path("add-classroom/", add_classroom, name="add_classroom"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
    path("person/<int:id>", person_detail, name="person_detail"),
]
