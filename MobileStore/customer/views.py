from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from mobile.models import Mobile, Cart
from django.views.generic import TemplateView


# Create your views here.

# def customer_home(request):
#     mobiles=Mobile.objects.all()
#     context={}
#     context["mobiles"]=mobiles
#     return render(request, "customer/home.html",context)

class CustomerHome(TemplateView):
    def get(self, request, *args, **kwargs):
        mobiles = Mobile.objects.all()
        context = {}
        context["mobiles"] = mobiles
        return render(request, "customer/home.html", context)


# def sign_up(request):
#     form = forms.UserRegistrationForm()
#     context = {"form": form}
#     # context["form"] = form
#     if request.method == "POST":
#         form = forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user has been registered")
#             return redirect("signin")
#         else:
#             context["form"] = form
#             return render(request, "user_registration.html", context)
#     return render(request, "user_registration.html", context)


class SignUp(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {"form": form}
        return render(request, "user_registration.html", context)

    def post(self, request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user has been registered")
            return redirect("signin")
        else:
            context = {"form": form}
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
#                 login(request, user)
#                 return redirect("customerhome")
#             else:
#                 return render(request, "login.html", {"form": form})
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
        mobile = Mobile.objects.get(id=id)
        cart = Cart.objects.create(item=mobile, user=request.user)
        print("item is added to cart")
        cart.save()
        return redirect("customerhome")

class MyCart(TemplateView):
    model=Cart
    template_name="mycart.html"
    context={}
    def get(self, request, *args, **kwargs):
        mycart=self.model.objects.filter(user=request.user)
        self.context["items"]=mycart
        return render(request,self.template_name,self.context)
