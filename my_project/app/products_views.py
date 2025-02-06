from django.shortcuts import render
from .models import products

def products_list(request):
    products_list = products.objects.all()  # Get all the products from the database
    return render(request, 'abc.html', {'products': products_list})  
