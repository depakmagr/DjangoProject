import requests
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response


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

#
# class PersonView(APIView):
#     def get(self):