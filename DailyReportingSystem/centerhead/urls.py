from django.urls import path
from centerhead import views

urlpatterns=[
    path("",views.AdminHome.as_view(),name="centerheadhome"),
    path("courses",views.Courses.as_view(),name="courses"),
    # path("courses/list",views.CourseList.as_view(),name="courselist"),
    path("batches",views.Batches.as_view(),name="batches"),
    path("updatecourse<int:id>",views.UpdateCourse.as_view(),name="courseupdate"),
    path("removecourse<int:id>",views.RemoveCourse.as_view(),name="courseremove"),
    path("viewcourse<int:id>",views.ViewCourse.as_view(),name="courseview"),

    path("updatebatch<int:id>",views.UpdateBatch.as_view(),name="batchupdate"),
    path("viewbatch<int:id>",views.ViewVBatch.as_view(),name="batchview")
]