from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, "users/home_page.html")

def newuser(request):
    return render(request, "user/newuser.html")

def login(request):
    response = Profile.objects.after_user_signed_up(request, user)
    if response == True:
        return redirect("/newuser")
    else:
        return redirect("/")
