import django_filters
from book.models import Book

class BookSearchFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=["book_name","price","copies","author"]
