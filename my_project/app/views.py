from django.shortcuts import render,HttpResponse

# Create your views here.

def sample(request):
    return render(request,'abc.html')
