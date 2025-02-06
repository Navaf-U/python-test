from django.shortcuts import render,HttpResponse
from .models import products

def products_view(request):
    j = products.objects.get()
    return HttpResponse(j)