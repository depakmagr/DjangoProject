from rest_framework.viewsets import ModelViewSet
from .viewsets import ListCreateUpdateDestroyViewSet
from .models import ClassRoom, Person
from .serializers import ClassRoomSerializer, PersonModelSerializer


class ClassRoomViewSet(ListCreateUpdateDestroyViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()


class PersonModelViewSet(ModelViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()