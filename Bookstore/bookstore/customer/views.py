from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from book.models import Book
from book.models import Cart
from django.contrib import messages


# Create your views here.

# def customer_home(request):
#     books=Book.objects.all()
#     context={"books":books}
#     return render(request,"customer/home.html",context)

class CustomerHome(TemplateView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, "customer/home.html", context)


# def sign_up(request):
#     form = forms.UserRegistrationForm
#     context = {"form": form}
#     if request.method == "POST":
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("signin")
#         else:
#             context["form"] = form
#             return render(request, "user_registration.html", context)
#     return render(request, "user_registration.html", context)

class SignUp(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm
        context = {"form": form}
        return render(request, "user_registration.html", context)

    def post(self, request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context = {}
            context["form"] = form
            return render(request, "user_registration.html", context)


# def signin(request):
#     form = forms.LoginForm()
#     context = {}
#     context["form"] = form
#     if request.method == "POST":
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 # if user exist aanenkil user nde session start cheyyanam.so call the login function
#                 login(request, user)
#                 return redirect("customerhome")
#             else:
#                 return render(request, "login.html", {"form": form})
#
#     return render(request, "login.html", context)

class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {}
        context["form"] = form
        return render(request, "login.html", context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                # if user exist aanenkil user nde session start cheyyanam.so call the login function
                login(request, user)
                return redirect("customerhome")
            else:
                return render(request, "login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("signin")


class AddToCart(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        book = Book.objects.get(id=id)
        cart = Cart.objects.create(item=book, user=request.user)
        cart.save()
        # print("item added to cart")
        messages.success(request,"item added to cart")
        return redirect("customerhome")


class MyCart(TemplateView):
    model = Cart
    template_name = "mycart.html"
    context = {}

    def get(self, request, *args, **kwargs):
        mycart = self.model.objects.filter(user=request.user,status="incart")
        self.context["items"] = mycart
        return render(request, self.template_name, self.context)


class RemoveItem(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart=Cart.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.success(request,"item has been removed")
        return redirect("customerhome")