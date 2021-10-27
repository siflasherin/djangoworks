from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from book.models import Book


# Create your views here.

def customer_home(request):
    books=Book.objects.all()
    context={"books":books}
    return render(request,"customer/home.html",context)


def sign_up(request):
    form = forms.UserRegistrationForm
    context={"form":form}
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "user_registration.html", context)
    return render(request, "user_registration.html", context)

def signin(request):
    form=forms.LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                # if user exist aanenkil user nde session start cheyyanam.so call the login function
                login(request,user)
                return redirect("customerhome")
            else:
                return render(request,"login.html",{"form":form})

    return render(request,"login.html",context)

def signout(request):
    logout(request)

    return redirect("signin")