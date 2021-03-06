from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.CustomerHome.as_view(), name="customerhome"),
    path("accounts/users/add", views.SignUp.as_view(), name="signup"),
    path("accounts/users/signin", views.SignIn.as_view(), name="signin"),
    path("accounts/users/signout", views.signout, name="signout"),
    path("books/addtocart<int:id>",views.AddToCart.as_view(),name="addtocart"),
    path("books/mycart",views.MyCart.as_view(),name="mycart"),
    path("books/removeitem<int:id>",views.RemoveItem.as_view(),name="removeitem"),
    path("books/buynow<int:id>",views.OrderCreate.as_view(),name="createorder"),
    path("books/myorders",views.ViewMyOrder.as_view(),name="myorders"),
]
