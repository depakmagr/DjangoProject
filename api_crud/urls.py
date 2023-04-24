from rest_framework.routers import DefaultRouter
from .views import ClassRoomViewSet, PersonModelViewSet

r = DefaultRouter()

r.register('classroom', ClassRoomViewSet, basename='classroom'),
r.register('person', PersonModelViewSet, basename='person'),


urlpatterns = r.urls
