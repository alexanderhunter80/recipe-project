from django.shortcuts import render, redirect, HttpResponse
from .models import Recipe, RecipeManager, Ingredient, Entry, Cookbook, Location #pylint: disable = E0402
from apps.users.models import Profile
import json
from django.http import JsonResponse
from django.contrib import messages



def populateBooks():

    # navbar will need list of cookbooks, prototype code here
    cookbooks = []
    cookList = Cookbook.objects.all()
    for c in cookList:
        cookbooks.append(c.name)
    print('list of cookbooks')
    print(cookbooks)
    return cookbooks



def new(request):

    cookbooks = populateBooks()

    context = {
        'cookbooks' : cookbooks
    }

    return render(request, 'recipes/addRecipe.html', context)



def create(request):
    print(request.POST)

    result = Recipe.objects.recipe_validator(request.POST)
    if result['status'] == True:
        for key, value in result['errors'].items():
            messages.error(request, value, extra_tags = key)
        return redirect('/recipes/new')
    else:
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

        newRecipe = Recipe.objects.create(name=allData['name'],steps=directList,notes=allData['notes'],user_id=request.user.id)
        print('creating new recipe')
        print(newRecipe)
        print(newRecipe.user.username)
        theirRecipes = Profile.objects.get(id=request.user.id).recipes.all()
        print(theirRecipes)
        for each in theirRecipes:
            print(each.name)
        for e in ingredList:
            if e['ingred'] in Ingredient.objects.all().values('name'):
                print('found ingredient in table')
                ingredLink = Ingredient.objects.get(name=e['ingred'])
            else:
                print('creating new ingredient')
                ingredLink = Ingredient.objects.create(name=e['ingred'])
            Entry.objects.create(qty=e['qty'],unit=e['units'],ingredient_id=ingredLink.id,recipe_id=newRecipe.id) 
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

    if request.method == 'GET':    

        r = Recipe.objects.get(id=n)
        print(r)
        ingList = []
        for e in r.entries.all():
            print(e)
            entry = {}
            entry['qty'] = e.qty
            entry['units'] = e.unit
            entry['name'] = e.ingredient.name
            ingList.append(entry)
        print(r.steps)
        print('list of ingredient rows')
        print(ingList)

        stepsList = r.steps.replace('[','')
        stepsList = stepsList.replace(']','')
        stepsList = stepsList.replace(" '",'')
        stepsList = stepsList.replace("'",'')
        stepsList = stepsList.split(',')
        print(stepsList)

        cookbooks = populateBooks()

        context = {
            'id' : r.id,
            'name' : r.name,
            'notes' : r.notes,
            'steps' : stepsList,
            'user' : r.user.username,
            'ingredients' : ingList,
            'cookbooks' : cookbooks,
            'recipeObject' : r
        }

        return render(request, 'recipes/showRecipe.html', context)

    elif request.method == 'DELETE':
        return HttpResponse("501 Not Implemented:  deleteRecipe")

    elif request.method == 'POST':

        r = Recipe.objects.get(id=n)

        result = Recipe.objects.recipe_validator(request.POST)
        if result['status'] == True:
            for key, value in result['errors'].items():
                messages.error(request, value, extra_tags = key)
            return redirect('/recipes/new')
        else:
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

            #r.update(name=allData['name'],steps=directList,notes=allData['notes'])
            r.name=allData['name']
            r.steps=directList
            r.notes=allData['notes']
            r.save()

            deleteEntries = r.entries.all()
            for each in deleteEntries:
                each.delete()

            for e in ingredList:
                if e['ingred'] in Ingredient.objects.all().values('name'):
                    print('found ingredient in table')
                    ingredLink = Ingredient.objects.get(name=e['ingred'])
                else:
                    print('creating new ingredient')
                    ingredLink = Ingredient.objects.create(name=e['ingred'])
                Entry.objects.create(qty=e['qty'],unit=e['units'],ingredient_id=ingredLink.id,recipe_id=r.id) # wtf do i do with this
            r.location.latitude=allData['lat']
            r.location.longitude=allData['lng']
            r.location.save()

            return redirect('/recipes/%s' % r.id)




def showAjax(request, n):

    r = Recipe.objects.get(id=n)

    dataDict = {
        'lat': r.location.latitude,
        'lng': r.location.longitude
    }

    return JsonResponse(dataDict)



def edit(request, n):

    r = Recipe.objects.get(id=n)
    print(r)
    ingList = []
    for e in r.entries.all():
        print(e)
        entry = {}
        entry['qty'] = e.qty
        entry['units'] = e.unit
        entry['name'] = e.ingredient.name
        ingList.append(entry)
    print('list of ingredient rows')
    print(ingList)
    print('notes')
    print(r.notes)

    stepsList = r.steps.replace('[','')
    stepsList = stepsList.replace(']','')
    stepsList = stepsList.replace(" '",'')
    stepsList = stepsList.replace("'",'')
    stepsList = stepsList.split(',')
    print(stepsList)

    cookbooks = populateBooks()

    context = {
        'recipeObject' : r,
        'id' : r.id,
        'name' : r.name,
        'notes' : r.notes,
        'steps' : stepsList,
        'user' : r.user.username,
        'ingredients' : ingList,
        'cookbooks' : cookbooks
    }

    return render(request, 'recipes/editRecipe.html', context)

def delete(request, n):
    recipe = Recipe.objects.get(id=n)
    recipe.delete()
    return redirect("/recipes")

def confirmDelete(request, n):
    context = {
        "id" : n
    }
    return render(request, "recipes/deleteRecipe.html", context)

def newBook(request):
    pass
    return render(request, 'recipes/addBook.html')

def createBook(request):
    pass
    return HttpResponse("501 Not Implemented: createBook")

def showBook(request, n):
    b = Cookbook.objects.get(id=n)
    context = {
        'id' : b.id,
        'name' : b.name,
        'user' : b.user
    }
    return render(request, "recipes/showBook.html", context)

def editBook(request, n):
    pass
    return HttpResponse("501 Not Implemented: editBook")

def deleteBook(request, n):
    cookbook = Cookbook.objects.get(id=n)
    cookbook.delete()
    return redirect("/recipes")

def confirmDeleteBook(request, n):
    context = {
        "id" : n
    }
    return render(result, "recipes/deleteBook.html", context)

def mapSearch(request):

    cookbooks = populateBooks()
    context = { 'cookbooks' : cookbooks}

    return render(request, 'recipes/mapSearch.html', context)

def mapSearchAjax(request):

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
    dataDict = {'markers':mapData}
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

def logout_view(request):
    logout(request)
    return redirect("/")