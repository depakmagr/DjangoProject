from django.shortcuts import render, redirect
from crud.models import Person
from .forms import PersonForm, PersonModelForm


# Create your views here.
def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)  #it runs validation
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            email = form.cleaned_data.get('email')
            department = form.cleaned_data.get('department')
            Person.objects.create(name=name, age=age, email=email, department=department)
            return redirect('home')
    context = {"form": PersonForm(), "title": "Create Person"}
    return render(request, "classbased/create_person.html", context)


def create_person_model_form(request):
    if request.method == "POST":
        form = PersonModelForm(request.POST)  #it runs validation
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": PersonModelForm(), "title": "Create Person using model form"}
    return render(request, "classbased/create_person_model_form.html", context)