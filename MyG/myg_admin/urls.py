from django.urls import path
from myg_admin import views
urlpatterns=[
    path("add",views.add_applience,name="addappliences"),
    path("list",views.list_applience,name="listappliences"),
    path("remove<int:id>",views.remove_applience,name="removeappliences"),
    path("view<int:id>",views.view_applience,name="viewappliences"),
]