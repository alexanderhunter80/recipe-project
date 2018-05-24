from django.shortcuts import render, redirect, HttpResponse
from .models import Recipe, RecipeManager, Ingredient, Entry, Cookbook, Location #pylint: disable = E0402
from apps.users.models import Profile 
import json
from django.http import JsonResponse



def new(request):

    # navbar will need list of cookbooks, prototype code here
    cookbooks = list(Cookbook.objects.all().name)
    print('list of cookbooks')
    print(cookbooks)

    context = {
        'cookbooks' : cookbooks
    }

    return render(request, 'recipes/addRecipe.html', context)



def create(request):
    print(request.POST)
    allData = request.POST.dict()
    ingredList = []
    directList = []
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

    newRecipe = Recipe.objects.create(name=allData['name'],steps=directList,notes=allData['notes'],user_id=1) # change this fake ass user_id
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
    print(newRecipe.name, newRecipe.notes, newRecipe.steps)
    print('its ingredients')
    print(newRecipe.entries.all().values())
    for e in list(newRecipe.entries.all()):
        print(e.ingredient.name)
    print('its location')
    print(newLocation.latitude, newLocation.longitude)

    return redirect('/recipes/new')



def show(request, n):

    if request.method == 'POST':    
        ##############################################
        # untested
        ##############################################

        r = Recipe.objects.get(id=n)
        ingList = []
        for e in list(Recipe.entries.all()):
            entry = {}
            entry['qty'] = e['qty']
            entry['units'] = e['units']
            entry['name'] = e.ingredient.name
            ingList.append(entry)
        print('list of ingredient rows')
        print(ingList)

        context = {
            'name' : r.name,
            'notes' : r.notes,
            'steps' : r.steps,
            # 'user' : user displayname,
            'ingredients' : ingList
        }

        return render(request, 'recipes/showRecipe.html', context)

    elif request.method == 'DELETE':
        return HttpResponse("501 Not Implemented:  deleteRecipe")

def edit(request, n):
    pass
    return HttpResponse("501 Not Implemented: edit")

def confirmDelete(request, n):
    pass
    return HttpResponse("501 Not Implemented: confirmDelete")

def newBook(request):
    pass
    return HttpResponse("501 Not Implemented: newBook")

def createBook(request):
    pass
    return HttpResponse("501 Not Implemented: createBook")

def showBook(reques, n):
    pass
    return HttpResponse("501 Not Implemented: showBook")

def editBook(request, n):
    pass
    return HttpResponse("501 Not Implemented: editBook")

def confirmDeleteBook(request, n):
    pass
    return HttpResponse("501 Not Implemented: confirmDeleteBook")

def mapSearch(request):
    pass
    return render(request, 'recipes/mapSearch.html')

def mapSearchAjax(request):

    ##########################################################################################################
    # UNTESTED 
    ##########################################################################################################

    allRecipes = Recipe.objects.all()
    mapData = []
    for r in allRecipes:
        entry = {}
        entry['id'] = r.id
        entry['name'] = r.name
        entry['notes'] = r.notes
        # entry['user'] = display name somehow
        entry['lat'] = r.location.latitude
        entry['lng'] = r.location.longitude
        mapData.append(entry)
    print(mapData)
    dataDict = {'mapData':mapData}
    return JsonResponse(dataDict)

def search(request):
    pass
    return HttpResponse("501 Not Implemented: search")

def searchResults(request):
    pass
    return HttpResponse("501 Not Implemented: searchResults")

# def ingSearch(request):
    # pass
    # return HttpResponse("501 Not Implemented")