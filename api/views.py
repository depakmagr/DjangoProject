import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from crud.models import Person
from .serializers import PersonSerializer, PersonModelSerializer


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
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Invalid input!!!!"
        }, status=status.HTTP_400_BAD_REQUEST)


class PersonModelSerializedView(APIView):
    def get(self, *args, **kwargs):
        person = Person.objects.all()
        serializer = PersonModelSerializer(person, many=True)     # this is serialization
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = PersonModelSerializer(data=self.request.data)  # this is diserialization
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"msg": serializer.errors})


class PersonListView(ListAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonListCreateView(ListCreateAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonRetrieveView(RetrieveAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonURDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()