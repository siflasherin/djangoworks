from django.urls import path
from customer import views

urlpatterns = [
    path("home", views.customer_home, name="customerhome"),
    path("accounts/users/add", views.sign_up, name="signup"),
    path("accounts/users/signin", views.signin, name="signin"),
    path("accounts/users/signout", views.signout, name="signout"),
]
