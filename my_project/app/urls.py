from django.urls import path
from .import views
from .import products_views

urlpatterns = [
    path('',views.sample),
    path('login/',views.login),
    path("products/",products_views.products_list),
]
