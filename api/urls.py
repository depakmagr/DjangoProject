from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import use_dummy_api, HelloWorld, PersonView, PersonSerializedView, PersonModelSerializedView,\
    PersonListView, PersonListCreateView, PersonRetrieveView, PersonURDView, PersonModelViewSet,\
    ClassRoomModelViewSet, PersonProfileModelViewSet

router = DefaultRouter()
router.register('person-viewset', PersonModelViewSet, basename='person_viewset')
router.register('classroom-viewset', ClassRoomModelViewSet, basename='classroom_viewset')
router.register('person-profile-viewset', PersonProfileModelViewSet, basename='person_profile_viewset')


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
] + router.urls