from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ClassRoom, Person, PersonProfile


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ClassRoomSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['name', 'uuid', 'created_at', 'updated_at']


class PersonSerializer(serializers.ModelSerializer):
    classroom = serializers.SlugRelatedField(slug_field="uuid",
                                             queryset=ClassRoom.objects.all())
    profile = serializers.SerializerMethodField()

    # classroom = ClassRoomSerializer()

    class Meta:
        model = Person
        read_only_fields = ['uuid', 'created_at', 'updated_at']
        fields = read_only_fields + ['name', 'email', 'age', 'classroom', 'is_active', 'profile']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["classroom"] = ClassRoomSerializer()

        # if request and request.method.lower() == "post":
        #     fields["classroom"] = classroom = serializers.SlugRelatedField(slug_field="uuid",
        #                                      queryset=ClassRoom.objects.all())
        return fields

    def get_profile(self, person_obj):
        try:
            profile = person_obj.person_profile
        except:
            return None
        ser = PersonProfileSerializer(profile)
        return ser.data


class PersonProfileSerializer(DynamicFieldsModelSerializer):
    person = serializers.SlugRelatedField(slug_field='uuid', queryset=Person.objects.all())

    class Meta:
        model = PersonProfile
        fields = ["uuid", "created_at", "updated_at", "person", "profile_picture",
                  "address"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == 'get':
            fields['person'] = PersonSerializer()
        return fields


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "is_superuser"]