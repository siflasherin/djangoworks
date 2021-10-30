from django.urls import path
from book import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/add", views.AddBook.as_view(), name="addbook"),
    path("book/list", views.ListBook.as_view(), name="listbook"),
    path("remove<int:id>", views.RemoveBook.as_view(), name="removebook"),
    path("update<int:id>",views.UpdateBook.as_view(),name="updatebook"),
    path("view<int:id>",views.BookView.as_view(),name="viewbook"),
]
