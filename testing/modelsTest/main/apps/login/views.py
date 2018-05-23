from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    response = "login page"
    return render(request, "login/login.html")