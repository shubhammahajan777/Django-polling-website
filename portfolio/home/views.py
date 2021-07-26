from django.db.models.fields import EmailField
from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is my home Page (/)")
    context = { 'name': 'Shubham', 'course': 'Django'}
    return render(request,'home.html', context)

def about(request):
    # return HttpResponse("This is my about Page (/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my projects Page (/projects)")
    return render(request,'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name = name, email = email, phone = phone, des = desc)
        ins.save()
        print("The data has been written to the db")
    # return HttpResponse("This is my contact Page (/contact)")
    return render(request,'contact.html')