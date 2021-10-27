from django.shortcuts import render, redirect
from myg_admin import forms
from myg_admin.models import Appliences


# Create your views here.
def add_applience(request):
    if request.method == "GET":
        form = forms.ApplienceAddForm()
        context = {}
        context["form"] = form
        return render(request, "add_appliences.html", context)
    if request.method == "POST":
        form = forms.ApplienceAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listappliences")
        else:
            context = {}
            context["form"] = form
            return render(request, "list_appliences.html", context)


def list_applience(request):
    appliences = Appliences.objects.all()
    context = {}
    context["appliences"] = appliences
    return render(request, "list_appliences.html", context)


def remove_applience(request, id):
    applience = Appliences.objects.get(id=id)
    applience.delete()
    return redirect("listappliences")

def view_applience(request,id):
    applience=Appliences.objects.get(id=id)
    context={}
    context["applience"]=applience
    return render(request,"view_appliences.html",context)
