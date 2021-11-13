from django.forms import ModelForm
from centerhead.models import Course,Batch

class CourseForm(ModelForm):
    class Meta:
        model=Course
        fields=["course_name"]


class BatchForm(ModelForm):
    class Meta:
        model=Batch
        fields=["course_name","batch_name"]
