from django.shortcuts import render, HttpResponse, redirect
from book.forms import BookAddForm,OrderUpdateForm,LoginForm
from book.models import Book,Orders
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout,authenticate,login
from django.utils.decorators import method_decorator
from book.decorators import signin_required
from book.filters import BookSearchFilter

# Create your views here.


def home(request):
    return render(request, "home.html")


# def add_book(request):
#     if request.method == "GET":
#         form = BookAddForm()
#
#         context = {}
#         context["form"] = form
#         return render(request, "add_book.html", context)
#
#     if request.method == "POST":
#         form = BookAddForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             # # print(form.cleaned_data)
#             # b_name=form.cleaned_data["book_name"]
#             # a_name=form.cleaned_data["author"]
#             # price=form.cleaned_data["price"]
#             # copies=form.cleaned_data["no_of_copies"]
#             # book=Book.objects.create(book_name=b_name,author=a_name,price=price,copies=copies)
#             # book.save()
#             # print("Book Saved")
#             # print(b_name,a_name,price,copies)
#             return redirect("listbook")
#         else:
#             context = {}
#             context["form"] = form
#             return render(request, "add_book.html", context)
#             # return render(request,"add_book.html",{"form":form})


# class AddBook(TemplateView):
#     def get(self, request, *args, **kwargs):
#         form = BookAddForm()
#         context = {}
#         context["form"] = form
#         return render(request, "add_book.html", context)
#
#     def post(self, request):
#         form = BookAddForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect("listbook")
#         else:
#             context = {}
#             context["form"] = form
#             return render(request, "add_book.html", context)

@method_decorator(signin_required,name="dispatch")
class AddBook(CreateView):
    model = Book
    form_class = BookAddForm
    template_name = "add_book.html"
    success_url = reverse_lazy("listbook")
    # to where we want to redirect
    # fields="__all__" to take all fields on form


# def list_book(request):
#     books = Book.objects.all()
#     context = {}
#     context["books"] = books
#     return render(request, "list_book.html", context)

# class ListBook(TemplateView):
#     def get(self, request, *args, **kwargs):
#         books = Book.objects.all()
#         context = {}
#         context["books"] = books
#         return render(request, "list_book.html", context)


@method_decorator(signin_required,name="dispatch")
class ListBook(ListView):
    model = Book
    template_name = "list_book.html"
    context_object_name = "books"


# def remove_book(request, id):
#     book = Book.objects.get(id=id)
#     book.delete()
#     return redirect("listbook")

# class RemoveBook(TemplateView):
#
#     def get(self, request, *args, **kwargs):
#         id = kwargs["id"]
#         book = Book.objects.get(id=id)
#         book.delete()
#         return redirect("listbook")


@method_decorator(signin_required,name="dispatch")
class RemoveBook(DeleteView):
    model = Book
    template_name = "remove_book.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")


# def update_book(request, id):
#     book = Book.objects.get(id=id)
#     if request.method == "GET":
#         # now we get blank form
#         form = BookAddForm(instance=book)
#         # initial={
#
#         # "book_name":book.book_name,
#         # 'author':book.author,
#         # "price":book.price,
#         # "no_of_copies":book.copies
#         # })
#         context = {}
#         context["form"] = form
#         return render(request, "update_book.html", context)
#
#     if request.method == "POST":
#         form = BookAddForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             # b_name = form.cleaned_data["book_name"]
#             # a_name = form.cleaned_data["author"]
#             # price = form.cleaned_data["price"]
#             # copies = form.cleaned_data["no_of_copies"]
#             # # book = Book.objects.create(book_name=b_name, author=a_name, price=price, copies=copies)
#             # book.book_name=b_name
#             # book.author = a_name
#             # book.price = price
#             # book.copies = copies
#             # book.save()
#             return redirect("listbook")

# class UpdateBook(TemplateView):
#     def get(self, request, *args, **kwargs):
#         id = kwargs["id"]
#         book = Book.objects.get(id=id)
#         form = BookAddForm(instance=book)
#         context = {}
#         context["form"] = form
#         return render(request, "update_book.html", context)
#
#     def post(self, request, *args, **kwargs):
#         id = kwargs["id"]
#         book = Book.objects.get(id=id)
#         form = BookAddForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect("listbook")


@method_decorator(signin_required,name="dispatch")
class UpdateBook(UpdateView):
    model = Book
    form_class = BookAddForm
    template_name = "update_book.html"
    success_url = reverse_lazy("listbook")
    pk_url_kwarg = "id"


# def book_view(request, id):
#     book = Book.objects.get(id=id)
#     context = {}
#     context["book"] = book
#     return render(request, "view_book.html", context)

# class BookView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         # book = Book.objects.get(id=id)
#         # context = {}
#         # context["book"] = book
#         # return render(request, "view_book.html", context)
#         context = {}
#         id = kwargs["id"]
#         book = Book.objects.get(id=id)
#         context["book"] = book
#         return render(request, "view_book.html", context)


@method_decorator(signin_required,name="dispatch")
class BookView(DetailView):
    model = Book
    template_name = "view_book.html"
    context_object_name = "book"
    pk_url_kwarg = "id"


@method_decorator(signin_required,name="dispatch")
class ViewOrders(ListView):
    model=Orders
    template_name = "customer_orders.html"
    context_object_name = "orders"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders=self.model.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        context["new_order_count"] = neworders.count()

        d_orders = self.model.objects.filter(status="delivered")
        context["d_orders"] = d_orders
        context["delivered_order_count"] = d_orders.count()

        return context


@method_decorator(signin_required,name='dispatch')
class DetailviewOrder(DetailView):
    model=Orders
    template_name = "customer_orderview.html"
    context_object_name = "order"
    pk_url_kwarg = "id"


@method_decorator(signin_required,name="dispatch")
class OrderUpdate(UpdateView):
    model=Orders
    form_class = OrderUpdateForm
    template_name = "orderchange.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("customerorders")


@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {}
        context["form"] = form
        return render(request, "adminlogin.html", context)

    def post(self, request):
        form =LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # if given credentials are valid ,return a user object
            user = authenticate(request, username=username, password=password)
            if user:
                # if user exist aanenkil user nde session start cheyyanam.so call the login function
                login(request, user)
                return redirect("listbook")
            else:
                return render(request, "adminlogin.html", {"form": form})

class BookSearch(TemplateView):
    model=Book
    template_name="books.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        f=BookSearchFilter(self.request.GET,queryset=Book.objects.all())
        # return render(request, 'books.html', {'filter': f})
        context["filter"]=f
        return context