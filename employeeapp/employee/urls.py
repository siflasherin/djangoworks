from django.urls import path
from employee import views

urlpatterns=[
    path("admin",views.Employee.as_view(),name="home"),
]