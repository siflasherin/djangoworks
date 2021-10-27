from django.urls import path
from mobile import views

urlpatterns = [
    path("",views.home,name="home"),
    path("mobile/add", views.add_mobile, name="addmobile"),
    path("mobile/list",views.list_mobile,name="listmobile"),
    path("remove<int:id>",views.remove_mobile,name="removemobile"),
    path("update<int:id>",views.update_mobile,name="updatemobile"),
    path("view<int:id>",views.view_mobile,name="mobileview"),

]
