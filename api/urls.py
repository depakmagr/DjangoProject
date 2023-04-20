from django.urls import path
from .views import use_dummy_api, HelloWorld, PersonView, PersonSerializedView, PersonModelSerializedView,\
    PersonListView, PersonListCreateView, PersonRetrieveView, PersonURDView


urlpatterns = [
    path("api-consumption/", use_dummy_api, name="use_dummy_api"),
    path("hello-world/", HelloWorld.as_view(), name="hello_world"),
    path("person/", PersonView.as_view(), name="person"),
    path("serialized-person/", PersonSerializedView.as_view(), name="serialized_person"),
    path("person-model-serialized/", PersonModelSerializedView.as_view(), name="person_model_serialized"),

    path("person-generic-list/", PersonListView.as_view(), name="person_generic_list"),
    path("person-generic/", PersonListCreateView.as_view(), name="person_generic"),
    path("person-retrieve-generic/<int:pk>", PersonRetrieveView.as_view(), name="person_retrieve-generic"),

    # in urd u=update, r=retrieve, d=delete/destroy
    path("person-urd/<int:pk>", PersonURDView.as_view(), name="person_urd")
]