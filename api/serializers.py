from rest_framework import serializers
from crud.models import Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    department = serializers.CharField()


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'department',]