from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ClassRoomViewSet, PersonViewSet, ClassRoomPersonView, PersonProfileViewSet,\
    UserViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CRUD API')


r = DefaultRouter()

r.register('classroom', ClassRoomViewSet, basename='classroom'),
r.register('person', PersonViewSet, basename='person'),
r.register('person-profile', PersonProfileViewSet, basename='person_profile'),
r.register('user', UserViewSet, basename='user'),


urlpatterns = [
    path("classroom/<str:uuid>/person/", ClassRoomPersonView.as_view,
         name="classroom_person"),
    path("login/", obtain_auth_token, name="login"),
    path("root/", schema_view)
] + r.urls
