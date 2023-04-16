from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"{user} created successfully !!")
            return redirect('login')
        else:
            messages.error(request, list(form.errors.values())[0])
            return redirect('register')
    # context = {"form": UserCreationForm()}
    context = {"form": CreateUserForm()}
    return render(request, "account/register.html", context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(request, username=un, password=pw)
        if user is not None:        #if user in authenticated
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect !!")
    return render(request, "account/login.html")


def logout_user(request):
    logout(request)
    return redirect('login')
