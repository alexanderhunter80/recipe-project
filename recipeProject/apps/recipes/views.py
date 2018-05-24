from django.shortcuts import render, redirect, HttpResponse
from .models import Recipe, RecipeManager, Ingredient, Entry, Cookbook, Location#pylint: disable = E0402
import json



def new(request):
    return render(request, 'recipes/addRecipe.html')



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

    newRecipe = Recipe.objects.create(name=allData['name'],step=directList,notes=allData['notes'])
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

    return redirect('/recipes/new')