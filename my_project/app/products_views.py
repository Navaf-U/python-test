from django.shortcuts import render,HttpResponse
from .models import products

def products_list(request):
    products_list = products.objects.all() 
    product_names = [product.name for product in products_list]
    return HttpResponse(product_names)
