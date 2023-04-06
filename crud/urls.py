from django.urls import path
from .views import *    # relative import.


urlpatterns = [
    path("create/", create, name="create"),
    path("file-test/", file_test, name="file_test"),
    path("classroom/", classroom, name="classroom"),
    path("add-classroom/", add_classroom, name="add_classroom"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", delete, name="delete"),
    path("", home, name='home'),
]
