from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    context = {"persons": Person.objects.all()}
    return render(request, template_name="crud/person.html", context=context)


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        status = True if request.POST.get("status") else False
        bio = request.POST.get("bio")
        profile_picture = request.FILES.get("pp")
        address = request.POST.get("address")
        class_room = request.POST.get("classroom")
        c = ClassRoom.objects.get(name=class_room)
        p = Person.objects.create(name=name, email=email, age=age, department=department, is_active=status)
        PersonProfile.objects.create(bio=bio, address=address, profile_picture=profile_picture, person=p, classroom=c)
        return redirect('home')
    context = {"title": "Add Person", "classroom": ClassRoom.objects.all()}
    return render(request, template_name="crud/create.html", context=context)


def update(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return redirect('home')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        status = True if request.POST.get("status") else False
        Person.objects.filter(id=id).update(name=name, email=email, age=age, department=department, is_active=status)
        return redirect('home')

    checked = "checked" if Person.is_active else ""

    context = {"title": "Update", "person": person, "checked": checked}
    return render(request, template_name="crud/update_person.html", context=context)


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExits:
        return redirect("home")

    if request.method == "POST":
        Person.objects.filter(id=id).delete()
        return redirect("home")

    context = {"title": "Delete Person", "person": person }
    return render(request, template_name="crud/delete_person.html", context=context)


def file_test(request):
    if request.method == 'POST':
        file = request.FILES.get("uploaded_file")
        FileStorage.objects.create(file=file, name=file.name)
        return redirect('file_test')

    context = {"infos": FileStorage.objects.all()}
    return render(request, template_name="crud/file_test.html", context=context)


def classroom(request):
    context = {"title": "Classrooms", "classes": ClassRoom.objects.all()}

    return render(request, template_name="crud/classroom.html", context=context)


def add_classroom(request):
    if request.method == 'POST':
        name = request.POST.get("classroom1")
        ClassRoom.objects.create(name=name)
        return redirect('classroom')

    context = {"title": "Add Classroom"}
    return render(request, template_name="crud/add_classroom.html", context=context)


def person_detail(request, id):
    try:
        person_profile = PersonProfile.objects.get(person_id=id)
    except PersonProfile.DoesNotExist:
        person_profile = None
    context = {"title": f"Detail View", "person_profile": person_profile}
    return render(request, "crud/detail_person.html", context=context)



