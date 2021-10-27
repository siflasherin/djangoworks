from django.urls import path
from centerhead import views

# from centerhead.views import add_batch
# from centerhead.views import add_faculty
# from centerhead.views import view_timesheet

urlpatterns = [
    path("",views.home,name="home"),
    path("accounts/signup", views.signup,name="signup"),
    path("accounts/signin", views.signin,name="signin"),
    path("courses/add", views.add_course,name="courseadd"),
    path("batches",views.list_batch,name="listbatch"),
    path("batches/add", views.add_batch,name="batchadd"),
    path("users",views.list_faculties,name="listfaculties"),
    path("users/add", views.add_faculty,name="usersadd"),
    path("timesheets", views.view_timesheet,name="viewtimesheet"),
    path("batches",views.list_batch,name="listbatch")

]
