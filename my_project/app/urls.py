from django.urls import path
from .import views

urlpatterns = [
    path('',views.sample),
    path('login/',views.login),
]
