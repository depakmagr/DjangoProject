from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    context = {"persons": Person.objects.all()}
    return render(request, template_name="crud/person.html", context=context)
