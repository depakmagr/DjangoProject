from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
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


class CreatePersonView(CreateView):
    model = Person
    template_name = "classbased/create_person_model_form.html"
    form_class = PersonModelForm
    success_url = reverse_lazy('home')

    # def post(self, request, *args, **kwargs):
    #     # send mail code.
    #     return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Create Person"
        return context


class PersonListView(ListView):
    # queryset = Person.objects.all()
    template_name = "classbased/person_list.html"
    context_object_name = "Person"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Person.objects.all()
        return Person.objects.all()[:5]


class PersonDetailView(DetailView):
    queryset = Person.objects.all()
    template_name = "classbased/person_detail_view.html"
    pk_url_kwarg = 'id'
    context_object_name = "person"

