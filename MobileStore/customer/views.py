from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from mobile.models import Mobile


# Create your views here.

def customer_home(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request, "customer/home.html",context)


def sign_up(request):
    form = forms.UserRegistrationForm()
    context = {"form": form}
    # context["form"] = form
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user has been registered")
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "user_registration.html", context)
    return render(request, "user_registration.html", context)


def signin(request):
    form = forms.LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("customerhome")
            else:
                return render(request, "login.html",{"form":form})
    return render(request, "login.html", context)

def signout(request):
    logout(request)
    return redirect("signin")