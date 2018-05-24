from django.shortcuts import render, redirect, HttpResponse
from .models import Recipe, RecipeManager, Ingredient, Entry, Cookbook, Location #pylint: disable = E0402
import json



def new(request):
    return render(request, 'recipes/addRecipe.html')



def create(request):
    print(request.POST)
    allData = request.POST.dict()
    ingredList = []
    directList = []
    thisLocation = {}
    for key in allData:
        if key == 'csrfmiddlewaretoken':
            continue
        elif 'qty' in key:
            ingredDict = {}
            ingredDict['qty'] = allData[key]
        elif 'units' in key:
            ingredDict['units'] = allData[key]
        elif 'ingred' in key:
            ingredDict['ingred'] = allData[key]
            ingredList.append(ingredDict)
        elif 'direct' in key:
            directList.append(allData[key])
        print('ingredList',ingredList)  
        print('directList',directList)

    newRecipe = Recipe.objects.create(name=allData['name'],step=directList,notes=allData['notes'],user_id=1) # change this fake ass user_id
    print('creating new recipe')
    print(newRecipe)
    for e in ingredList:
        if e['ingred'] in Ingredient.objects.all().values('name'):
            print('found ingredient in table')
            ingredLink = Ingredient.objects.get(name=e['ingred'])
        else:
            print('creating new ingredient')
            ingredLink = Ingredient.objects.create(name=e['ingred'])
        Entry.objects.create(qty=e['qty'],unit=e['units'],ingredient_id=ingredLink,recipe_id=newRecipe) 
    newLocation = Location.objects.create(latitude=allData['lat'],longitude=allData['lng'],recipe=newRecipe)

    # test printouts
    print('new recipe')
    print(newRecipe.name, newRecipe.notes, newRecipe.step)
    print('its ingredients')
    print(newRecipe.ingredient_entry.all().values())
    print(newRecipe.ingredient_entry.all().ingredient_id.all())
    print('its location')
    print(newRecipe.location.latitude, newRecipe.location.longitude)

    return redirect('/recipes/new')



def show(request, n):
    pass
    return HttpResponse("501 Not Implemented: Show")

def edit(request, n):
    pass
    return HttpResponse("501 Not Implemented")

def confirmDelete(request, n):
    pass
    return HttpResponse("501 Not Implemented")

def newBook(request):
    pass
    return HttpResponse("501 Not Implemented")

def createBook(request):
    pass
    return HttpResponse("501 Not Implemented")

def showBook(reques, n):
    pass
    return HttpResponse("501 Not Implemented")

def editBook(request, n):
    pass
    return HttpResponse("501 Not Implemented")

def confirmDeleteBook(request, n):
    pass
    return HttpResponse("501 Not Implemented")

def mapSearch(request):
    pass
    return render(request, 'recipes/mapSearch.html')

def mapSearchAjax(request):
    pass
    return HttpResponse("501 Not Implemented")

def search(request):
    pass
    return HttpResponse("501 Not Implemented")

def searchResults(request):
    pass
    return HttpResponse("501 Not Implemented")

# def ingSearch(request):
    # pass
    # return HttpResponse("501 Not Implemented")