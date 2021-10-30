from django.urls import path
from mobile import views

urlpatterns = [
    path("",views.home,name="home"),
    path("mobile/add", views.AddMobile.as_view(), name="addmobile"),
    path("mobile/list",views.ListMobile.as_view(),name="listmobile"),
    path("remove<int:id>",views.RemoveMobile.as_view(),name="removemobile"),
    path("update<int:id>",views.UpdateMobile.as_view(),name="updatemobile"),
    path("view<int:id>",views.ViewMobile.as_view(),name="mobileview"),

]
