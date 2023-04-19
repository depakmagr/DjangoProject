import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from rest_framework.views import APIView
from rest_framework.response import Response

from crud.models import Person
from .serializers import PersonSerializer


# Create your views here.
def use_dummy_api(request):
    API_URL = "https://dummyjson.com/product/1"
    response = requests.get(API_URL)
    response = response.json()
    print(response)
    context = {"iphone": response}
    return render(request, "api/dummy_api.html", context)


class HelloWorld(APIView):
    def get(self, request, *args, **kwargs):
        response = {"messege": "Hello World from rest framework"}
        return Response(response)


class PersonView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.GET.get("name")
        if name:
            persons = Person.objects.filter(name=name)
        else:
            persons = Person.objects.all()
        response = []
        for person in persons:
            response.append({
                "name": person.name,
                "age": person.age
            })
        return Response(response)
        # return Response({
        #     "name": person.name,
        #     "age": person.age,
        #     "email": person.email,
        #     "department": person.department
        # })


class PersonSerializedView(APIView):
    def get(self, *args, **kwargs):
        # person = Person.objects.get(id=1)
        person = Person.objects.all()
        # This step is not required if we use serializer
        # response = {
        #     "name": person.name,
        #     "age": person.age,
        # }
        serializer = PersonSerializer(person, many=True)     # this is serialization
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PersonSerializer(data=data)   # this is diserialization
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            age = serializer.validated_data.get('age')
            department = serializer.validated_data.get('department')
            Person.objects.create(name=name, email=email, age=age, department=department)
            return Response({
                "message": "Person created successfully!!"
            })
        return Response({
            "message": "Invalid input!!!!"
        })