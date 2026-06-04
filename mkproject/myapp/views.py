
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Student


def home(request):
    return HttpResponse ("Hello Django !")

def detail(request, post_id):
    return HttpResponse(f"You are viewing post detail page ,ID is {post_id}")

def hello(request):
    return render(request,'hello.html')

def profile(request):
    context = {
        'name'  : 'AJAY',
        'age'   : 26,
        'skills': ['Python', 'Django', 'HTML'],
    }
    return render(request, 'profile.html', context)

def old_url_redirect(request):
    return redirect(reverse('myapp:new_page_url'))

def new_url_view(request):
    return HttpResponse('this is the new url')

def Home(request):
    return render(request,'Home.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    context = {
        'name'  : "AJAY SUNDARAM . A",
        'age'   : 26,
        'skills': ['Python', 'Django', 'HTML'],
    }   
    return render(request,'about.html',context)

def css_one(request):
    return render(request,'css_one.html')


# VIEW ALL
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

# ADD
def add_student(request):
    if request.method == "POST":
        name  = request.POST['name']
        age   = request.POST['age']
        email = request.POST['email']
        Student.objects.create(name=name, age=age, email=email)
        return redirect('myapp:student_list')
    return render(request, 'add.html')

# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name  = request.POST['name']
        student.age   = request.POST['age']
        student.email = request.POST['email']
        student.save()
        return redirect('myapp:student_list')
    return render(request, 'update.html', {'student': student})

# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('myapp:student_list')


