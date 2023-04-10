from django.shortcuts import render, redirect
from .forms import CreateUserForm
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register_user(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    # context = {"form": UserCreationForm()}
    context = {"form": CreateUserForm()}
    return render(request, "account/register.html", context)


def login_user(request):
    return render(request, "account/login.html")
