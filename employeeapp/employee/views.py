from django.shortcuts import render
from django.views.generic import TemplateView
from employee.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class Employee(TemplateView):
    def get(self, request, *args, **kwargs):
        form=LoginForm()
        context={}
        context["form"]=form
        return render(request,'login.html',context)
    def post(self,request):
        form = LoginForm()
        context={}
        context["form"] = form
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"home.html",context)
            else:
                return render(request,"login.html",context)



