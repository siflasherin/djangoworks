from django.shortcuts import render, redirect
from customer import forms
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,ListView
from book.models import Book
from book.models import Cart, Orders
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
        messages.success(request, "item added to cart")
        return redirect("customerhome")


class MyCart(TemplateView):
    model = Cart
    template_name = "mycart.html"
    context = {}

    def get(self, request, *args, **kwargs):
        mycart = self.model.objects.filter(user=request.user, status="incart")
        self.context["items"] = mycart
        return render(request, self.template_name, self.context)


class RemoveItem(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        cart = Cart.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        messages.success(request, "item has been removed")
        return redirect("customerhome")


class OrderCreate(TemplateView):
    model = Orders
    form_class = forms.OrderForm
    template_name = "createorder.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        cid = kwargs["id"]
        cart_item = Cart.objects.get(id=cid)
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            user = request.user.username
            item = cart_item.item
            order = self.model.objects.create(
                address=address,
                item=item,
                user=user
            )
            order.save()
            cart_item.status = "orderplaced"
            cart_item.save()
            messages.success(request, "your order has been placed")
            return redirect("customerhome")


# class MyOrders(TemplateView):
#     model = Orders
#     template_name = "myorders.html"
#     context = {}
#
#     def get(self, request, *args, **kwargs):
#         myorder = Orders.objects.filter(user=request.user, status="orderplaced")
#         self.context["items"] = myorder
#         return render(request, self.template_name, self.context)

class ViewMyOrder(ListView):
    model=Orders
    template_name = "myorders.html"
    context_object_name = "orders"
    def get_queryset(self):
        queryset=super().get_queryset()
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset