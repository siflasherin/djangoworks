from django import forms

class CourseForm(forms.Form):
    course_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


class BatchForm(forms.Form):
    course_name=forms.CharField()
    batch_name=forms.CharField()

class Reg(forms.Form):
    user_name=forms.CharField()
    first_name=forms.CharField()
    email=forms.CharField()
    password=forms.CharField()
    phone=forms.CharField()

class Login(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField()













