from django.urls import path
from book import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/add", views.add_book, name="addbook"),
    path("book/list", views.list_book, name="listbook"),
    path("remove<int:id>", views.remove_book, name="removebook"),
    path("update<int:id>",views.update_book,name="updatebook"),
    path("view<int:id>",views.book_view,name="viewbook"),
]
