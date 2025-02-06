from django.shortcuts import render,HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse('hello world')
