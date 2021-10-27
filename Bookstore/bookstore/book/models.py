from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(unique=True,max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=50)
    copies=models.PositiveIntegerField(default=50,null=True)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.book_name


class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    options=(
        ("incart","incart"),
        ("cancelled","cancelled"),
        ("order placed","order placed")
    )
    status=models.CharField(max_length=100,choices=options,default="incart")

# orm (object relational mapping)
#
#create model
# book=Book(book_name="alchemist",author="abcd",price=23,copies=344)
# book=Book(book_name="india in my dreams",author="Gandhi",price=500,copies=100)
# book=Book.objects.create(book_name="india in my dreams",author="Gandhi",price=500,copies=100)


# fetch all objects from db
# select * from table (in normal sql) instead in django we must use ORM queries
# books=Book.objects.all()   (we pass this value as key in context)

# to fetch all details of a book
# for book in books:
#     print(book.book_name,book.price)

# print all books price < 300
# books=Book.objects.filter(price__lt=300)

# print book price b/w 300 to 350 range
# book=Book.objects.filter(price__gt=100,price__lt=300)

# case in-sensitivity check
# by default checks the exact match.to get name of a book even we dont mind about the case sensitivity
# book=Book.objects.filter(book_name__iexact="Alchemist")

# to delete an entry or to fetch a particular object --------update ,delete, view
# book=Book(book_name="test1",author="test2",price=233,copies=34)
# book=Book.objects.get(book_name="test1"
# book.delete()

# >>> books=Book.objects.all().values('id','book_name')
# >>> books

# update ORM Query
# book=Book.objects.get(id=3)
# book.price=350
# book.copies=300
# book.save()


# python3 manage.py createsuperuser