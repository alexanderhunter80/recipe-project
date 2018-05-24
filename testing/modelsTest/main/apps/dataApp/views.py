from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    response = "testing"
    print(Profile.objects.get(id=2).OAuth_info.first_name)
    temp = Profile.objects.get(id=2).OAuth_info
    temp.username = "GrizzleyBear"
    temp.save()
    print(temp.username)
    return render(request, "dataApp/index.html")
    
def create(request):
    response = Recipe.objects.recipe_validator(request.POST)
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/', messages)    
    else:
        return redirect('/recipe')

def recipe(request):

    return render(request, "dataApp/recipe.html")