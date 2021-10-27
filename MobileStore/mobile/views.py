from django.shortcuts import render, redirect
from mobile.forms import MobileAddForm
from mobile.models import Mobile


# Create your views here.

def home(request):
    return render(request, "home.html")


def add_mobile(request):
    if request.method == "GET":
        form = MobileAddForm()

        context = {}
        context["form"] = form

        return render(request, "add_mobile.html", context)

    if request.method == "POST":
        form = MobileAddForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            # m_name = form.cleaned_data["mobile_name"]
            # model = form.cleaned_data["model"]
            # color = form.cleaned_data["colour"]
            # ram = form.cleaned_data["storage"]
            # copies = form.cleaned_data["copies"]
            # price = form.cleaned_data["price"]
            # mobile = Mobile.objects.create(mobile_name=m_name, model=model, colour=color, storage=ram, copies=copies,
            #                                price=price)
            # mobile.save()
            # print("New Mobile Saved Succsessfully....")
            # # print(m_name,model,color,ram,copies,price)
            return redirect("listmobile")
        else:
            return render(request, "add_mobile.html", {"form": form})
            # context


def list_mobile(request):
    mobiles = Mobile.objects.all()
    # mobiles.save()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "list_mobile.html", context)


def remove_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobile")


def update_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    if request.method == "GET":
        form = MobileAddForm(instance=mobile
                             #     initial={
                             #     "mobile_name": mobile.mobile_name,
                             #     "model": mobile.model,
                             #     "colour": mobile.colour,
                             #     "storage": mobile.storage,
                             #     "copies": mobile.copies,
                             #     "price": mobile.price,
                             # }
                             )
        context = {}
        context["form"] = form
        return render(request, "update_mobile.html", context)
    if request.method == "POST":
        form = MobileAddForm(request.POST, instance=mobile)
        if form.is_valid():
            form.save()
            # m_name = form.cleaned_data["mobile_name"]
            # model = form.cleaned_data["model"]
            # color = form.cleaned_data["colour"]
            # ram = form.cleaned_data["storage"]
            # copies = form.cleaned_data["copies"]
            # price = form.cleaned_data["price"]
            #
            # mobile.mobile_name = m_name
            # mobile.model = model
            # mobile.colour = color
            # mobile.storage = ram
            # mobile.copies = copies
            # mobile.price = price
            # mobile.save()
            return redirect("listmobile")

def view_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"view_mobile.html",context)
