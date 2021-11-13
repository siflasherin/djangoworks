from django.urls import path
from book import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/add", views.AddBook.as_view(), name="addbook"),
    path("book/list", views.ListBook.as_view(), name="listbook"),
    path("remove<int:id>", views.RemoveBook.as_view(), name="removebook"),
    path("update<int:id>", views.UpdateBook.as_view(), name="updatebook"),
    path("view<int:id>", views.BookView.as_view(), name="viewbook"),
    path("customerorderslist", views.ViewOrders.as_view(), name="customerorders"),
    path("cusorderview<int:id>", views.DetailviewOrder.as_view(), name="customerorderview"),
    path("orders/change<int:id>", views.OrderUpdate.as_view(), name="orderchange"),
    path("accounts/signout", views.signout, name="signout"),
    path("signin",views.SignIn.as_view(),name="adminsignin"),
    path("find",views.BookSearch.as_view(),name="bookfilter"),

]
# {%extends "customer/base.html"%}
#
# {%block body_block%}
# {%endblock%}
