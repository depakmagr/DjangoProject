from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClassRoomViewSet, PersonViewSet, ClassRoomPersonView, PersonProfileViewSet

r = DefaultRouter()

r.register('classroom', ClassRoomViewSet, basename='classroom'),
r.register('person', PersonViewSet, basename='person'),
r.register('person-profile', PersonProfileViewSet, basename='person_profile'),


urlpatterns = [
    path("classroom/<str:uuid>/person/", ClassRoomPersonView.as_view,
         name="classroom_person")
] + r.urls
