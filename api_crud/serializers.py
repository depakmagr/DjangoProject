from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ClassRoom, Person, PersonProfile


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['name', 'uuid', 'created_at', 'updated_at']


class PersonSerializer(serializers.ModelSerializer):
    classroom = serializers.SlugRelatedField(slug_field="uuid",
                                             queryset=ClassRoom.objects.all())

    # classroom = ClassRoomSerializer()

    class Meta:
        model = Person
        read_only_fields = ['uuid', 'created_at', 'updated_at']
        fields = read_only_fields + ['name', 'email', 'age', 'classroom', 'is_active']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["classroom"] = ClassRoomSerializer()

        # if request and request.method.lower() == "post":
        #     fields["classroom"] = classroom = serializers.SlugRelatedField(slug_field="uuid",
        #                                      queryset=ClassRoom.objects.all())
        return fields


class PersonProfileSerializer(serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field='uuid', queryset=Person.objects.all())

    class Meta:
        model = PersonProfile
        fields = ["uuid", "created_at", "updated_at", "person", "profile_picture",
                  "address"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "is_superuser"]