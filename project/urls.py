from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path("home", views.index, name='home'),
    path("login", views.loginuser, name='login'),
    path("logout", views.logoutuser, name='logout'),
]
