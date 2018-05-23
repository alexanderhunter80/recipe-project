from django.shortcuts import render, redirect, HttpResponse
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


    return redirect('/recipes/new')