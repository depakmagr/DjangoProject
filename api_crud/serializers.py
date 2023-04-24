from rest_framework import serializers
from .models import ClassRoom, Person


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['name', 'uuid', 'created_at', 'updated_at']


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        read_only_fields = ['uuid', 'created_at', 'updated_at']
        fields = read_only_fields + ['name', 'email', 'age', 'classroom', 'is_active']