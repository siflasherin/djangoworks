from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=50,unique=True)
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    course_name=models.ForeignKey(to=Course,on_delete=models.CASCADE)
    batch_name=models.CharField(max_length=100,unique=True)
    active_status=models.BooleanField(default=True)