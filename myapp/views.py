from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader


def home(request):
    # print(dir(request))
    print(request.method)
    print(request.headers)
    print(request.is_secure())
    print(request.scheme)
    name = (request.GET.get('name'))
    age = (request.GET.get('age'))
    return HttpResponse(f"<h1>Hello my name is {name} and I am {age} years old.</h1>")


def name_func(request, name):
    data = {
        "deepak": "DEEPAK BAHADUR",
        "gabriel": "GABRIEL KUMAR"
    }
    # try:
    #     name = data[name]
    # except KeyError:
    #     pass
    name = data.get(name)
    if not name:
        return HttpResponseNotFound("Invalid URL")
    return HttpResponse(f"<h1>Hello i am {name}!</h1>")


def template(request):
    template = loader.get_template("home.html")
    context = {"name": "Deeps", "age": 234, "hobbies": ['Sports', 'Reading', 'Movies']}
    template_data = template.render(context, request)
    return HttpResponse(template_data)
    # return render(request, template_name="myapp/home.html")


# def inside_template(request):
#     return render(request, template_name="myapp/inside.html")


def students(request):
    context = {
        "Infos": [
        {
            "name": "Deepak Magar",
            "age": 25,
            "department": "CA",
        },
        {
            "name": "Gabriel Muktan",
            "age": 16,
            "department": "BCA",
        },
        {
            "name": "Nobel Rai",
            "age": 21,
            "department": "CSA",
        },
        {
            "name": "Prakash Magar",
            "age": 29,
            "department": "ICA",
        }
        ]
    }
    return render(request, "students.html", context)


def index(request):
    return render(request, template_name="index.html")