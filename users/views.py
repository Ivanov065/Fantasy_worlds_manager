from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        else:
            errors = form.errors
            return render(request, "register.html", {"form": form, "errors":errors})
        
    form = RegisterForm()
    return render(request, "register.html", {"form": form})

def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("node_manager:home")
        else:
            errors = form.errors
            return render(request, "login.html", {"form": form, "errors" : errors})
        
    form = LoginForm()
    return render(request, "login.html", {"form": form})

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("node_manager:home")

    return render(request, "logout.html")
