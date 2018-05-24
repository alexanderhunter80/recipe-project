from django.shortcuts import render, HttpResponse, redirect
# from .models import *
from django.contrib import messages

def index(request):
    return render(request, "users/home_page.html")