from django.shortcuts import render,HttpResponse
from .models import register

# Create your views here.

def sample(request):
    return render(request,'abc.html')

def login(request):
    j = register.objects.get(name="irfan")
    return HttpResponse("name "+ j.name + "\n" + "email " + j.email)