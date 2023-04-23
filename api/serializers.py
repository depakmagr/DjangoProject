from rest_framework import serializers
from crud.models import Person, ClassRoom, PersonProfile


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    department = serializers.CharField()


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'email', 'department',]


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class PersonProfileModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    # person = PersonSerializer()

    class Meta:
        model = PersonProfile
        fields = ['id', 'person', 'profile_picture', 'bio', 'address','classroom',]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method.lower() == "get":
            fields["person"] = PersonSerializer()
        return fields





