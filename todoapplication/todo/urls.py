from django.urls import path
from todo import views
urlpatterns = [
    path("add",views.add_todo) ,
    path("list",views.list_todo)
    ]
