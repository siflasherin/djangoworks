from django.shortcuts import render,HttpResponse,redirect
from book.forms import BookAddForm
from book.models import Book

# Create your views here.


def home(request):
    return render(request,"home.html")

def add_book(request):
    if request.method=="GET":
        form=BookAddForm()

        context={}
        context["form"]=form
        return render(request,"add_book.html",context)

    if request.method=="POST":
        form=BookAddForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            # # print(form.cleaned_data)
            # b_name=form.cleaned_data["book_name"]
            # a_name=form.cleaned_data["author"]
            # price=form.cleaned_data["price"]
            # copies=form.cleaned_data["no_of_copies"]
            # book=Book.objects.create(book_name=b_name,author=a_name,price=price,copies=copies)
            # book.save()
            # print("Book Saved")
            # print(b_name,a_name,price,copies)
            return redirect("listbook")
        else:
            context={}
            context["form"]=form
            return render(request,"add_book.html",context)
            # return render(request,"add_book.html",{"form":form})

def list_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"list_book.html",context)

def remove_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("listbook")

def update_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=="GET":
        # now we get blank form
        form=BookAddForm(instance=book)
            # initial={

            # "book_name":book.book_name,
            # 'author':book.author,
            # "price":book.price,
            # "no_of_copies":book.copies
        # })
        context={}
        context["form"]=form
        return render(request,"update_book.html",context)

    if request.method=="POST":
        form=BookAddForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            # b_name = form.cleaned_data["book_name"]
            # a_name = form.cleaned_data["author"]
            # price = form.cleaned_data["price"]
            # copies = form.cleaned_data["no_of_copies"]
            # # book = Book.objects.create(book_name=b_name, author=a_name, price=price, copies=copies)
            # book.book_name=b_name
            # book.author = a_name
            # book.price = price
            # book.copies = copies
            # book.save()
            return redirect("listbook")

def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"view_book.html",context)