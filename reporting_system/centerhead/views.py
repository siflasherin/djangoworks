from django.shortcuts import render, HttpResponse, redirect
from centerhead.forms import CourseForm, BatchForm,Reg,Login


# Create your views here.


def home(request):
    return render(request, "home.html")

#
# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get("u_name")
#         firstname = request.POST.get("f_name")
#         email = request.POST.get("email")
#         password = request.POST.get("pwd")
#         phone_no = request.POST.get("phone")
#         print(username, firstname, email, password, phone_no)
#         return render(request, "registration.html")
#
#     return render(request, "registration.html")

def signup(request):
    if request.method=="GET":
        form=Reg()
        context={}
        context["form"]=form
        return render(request,"registration.html",context)

    if request.method=="POST":
        form=Reg(request.POST)

        if form.is_valid():
            u_name=form.cleaned_data["user_name"]
            f_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            phone = form.cleaned_data["phone"]
            print(u_name,f_name,email,pwd,phone)
        return redirect("signup")


# def signin(request):
#     if request.method == "POST":
#         username = request.POST.get("u_name")
#         password = request.POST.get("pwd")
#         print(username, password)
#         return render(request, "login.html")
#
#     return render(request, "login.html")

def signin(request):
    if request.method=="GET":
        form=Login()

        context={}
        context["form"]=form
        return render(request,"login.html",context)

    if request.method=="POST":
        form=Login(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data["user_name"]
            pwd=form.cleaned_data["password"]
            print(u_name,pwd)
        return redirect("signin")

# def add_course(request):
#     if request.method == "POST":
#         # print(request.POST)
#         # csrf middle ware token(for security check),text box's name ,values from the text boxes,
#         course_name = request.POST.get("c_name")
#         print(course_name)
#         return render(request, 'add_course.html')
#     return render(request, 'add_course.html')

def add_course(request):
    if request.method == "GET":
        form = CourseForm()

        context = {}
        context["form"] = form

        return render(request, "add_course.html", context)

    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            # # {'course_name': 'python'}

            c_name = form.cleaned_data["course_name"]
            print(c_name)
        return redirect("courseadd")
        # return render(request, "add_course.html")


def add_batch(request):
    if request.method == "GET":
        form = BatchForm()

        context = {}
        context["form"] = form
        return render(request, "add_batch.html", context)

    if request.method == "POST":
        form = BatchForm(request.POST)

        if form.is_valid():

            c_name = form.cleaned_data["course_name"]
            b_name = form.cleaned_data["batch_name"]
            print(c_name, b_name)
        return redirect("batchadd")


# def add_batch(request):
#     if request.method=="POST":
#         course=request.POST.get("c_name")
#         batch=request.POST.get("b_name")
#         print(course,batch)
#         return render(request,"add_batch.html")
#
#     return render(request, "add_batch.html")


def add_faculty(request):
    if request.method == "POST":
        faculty = request.POST.get("f_name")
        batch = request.POST.get("b_name")
        print(faculty, batch)
        return render(request, "add_faculty.html")

    return render(request, "add_faculty.html")


def view_timesheet(request):
    timesheets = [
        {"user": "user1", "topic": "djangoforms", "complted": "true"},
        {"user": "user2", "topic": "drf", "complted": "true"},
        {"user": "user3", "topic": "drf", "complted": "true"},

    ]
    context = {}
    context["timesheets"] = timesheets
    return render(request, "list_timesheets.html", context)


def list_batch(request):
    batches = [
        {"batch_code": "DJ-JUL-2k21", "batch_name": "djangojuly", "students": 25},
        {"batch_code": "DJ-AUG-2k21", "batch_name": "djangoaugest", "students": 30},
        {"batch_code": "MS-AUG-2k21", "batch_name": "meanstackaug", "students": 32},

    ]
    context = {}
    context["batches"] = batches
    return render(request, "list_batches.html", context)


def list_faculties(request):
    users = [
        {"user_name": "sabir", "domain": "BIG DATA"},
        {"user_name": "shifna", "domain": "DJANGO"},
        {"user_name": "rugma", "domain": "TESTING"}

    ]

    context = {}
    context["users"] = users

    return render(request, "list_faculties.html", context)


