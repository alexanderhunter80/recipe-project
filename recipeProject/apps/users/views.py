from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, "users/home_page.html")

def newuser(request):
    return render(request, "users/newuser.html")

def login(request):
    user_id = request.user.id
    user = Profile.objects.get(id=user_id)
    # user.username = ""
    # user.save()
    if not user.username:
        return redirect("/newuser")
    else:
        return redirect("/")

def create_username(request):
    user_id = request.user.id
    user = Profile.objects.get(id=user_id)
    auth_user = User.objects.get(id=user_id)
    user.username = request.POST['username']
    user.save()
    auth_user.username = request.POST['username']
    auth_user.save()
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.INFO, "Successfully logged in as " + user.username + ".")
    return redirect("/")

