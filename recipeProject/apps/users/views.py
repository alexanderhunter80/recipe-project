from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    # @receiver(post_save, sender=User)
    # def create_new_user(sender, instance, created, **kwargs):
    # if created:
    #     return redirect("/newuser")
    return render(request, "users/home_page.html")

def newuser(request):
    return render()
