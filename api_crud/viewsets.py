from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListCreateUpdateDestroyViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class CreateUpdateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass