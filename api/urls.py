from django.urls import path
from .views import use_dummy_api, HelloWorld, PersonView, PersonSerializedView

urlpatterns = [
    path("api-consumption/", use_dummy_api, name="use_dummy_api"),
    path("hello-world/", HelloWorld.as_view(), name="hello_world"),
    path("person/", PersonView.as_view(), name="person"),
    path("serialized-person/", PersonSerializedView.as_view(), name="serialized_person"),
]