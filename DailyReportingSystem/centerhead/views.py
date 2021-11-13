from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView,UpdateView,DeleteView,DetailView
from centerhead import forms
from centerhead.models import Course, Batch
from django.urls import reverse_lazy


# Create your views here.

class AdminHome(TemplateView):
    template_name = "centerhead/adminhome.html"


class Courses(CreateView):
    model = Course
    template_name = "centerhead/courses.html"
    form_class = forms.CourseForm
    success_url = reverse_lazy("courses")

    # context_object_name = "courses" .instead of this we mentioned at context section

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = self.model.objects.all()
        return context


class Batches(CreateView):
    model = Batch
    success_url = reverse_lazy("batches")
    template_name = "centerhead/batches.html"
    form_class =forms.BatchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["batches"] = self.model.objects.all()
        return context

class UpdateCourse(UpdateView):
    model=Course
    template_name = "centerhead/update_course.html"
    success_url = reverse_lazy("courses")
    form_class = forms.CourseForm
    pk_url_kwarg = "id"

class RemoveCourse(DeleteView):
    model=Course
    template_name = "centerhead/remove_course.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("courses")

class ViewCourse(DetailView):
    model=Course
    template_name = "centerhead/view_course.html"
    pk_url_kwarg = "id"

class UpdateBatch(UpdateView):
    model=Batch
    template_name = "centerhead/update_batch.html"
    form_class = forms.BatchForm
    success_url = reverse_lazy("batches")
    pk_url_kwarg = "id"


class ViewVBatch(DetailView):
    model = Batch
    template_name = "centerhead/view_batch.html"
    pk_url_kwarg = 'id'
