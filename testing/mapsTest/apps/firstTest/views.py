from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
import json
from .models import Location, LocationManager #pylint: disable = E0402




def index(request):

    return render(request, 'firstTest/index.html')





def embed(request):

    # render page as normal first
    # have JS make an AJAX call to a new, AJAX-only route
    # AJAX route returns a dictionary using syntax:  return JsonResponse({'foo':'bar'})


    return render(request, 'firstTest/embedded.html') 



def addLoc(request):
    pass



def jsonReceiver(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            jData = json.loads(request.body)
            print(jData)
            print('lat '+str(jData['lat']))
            print('lng '+str(jData['lng']))
            latDec = round(jData['lat'],4)
            lngDec = round(jData['lng'],4)
            print('rounded lat '+str(latDec))
            print('rounded lng '+str(lngDec))
            newLoc = Location.objects.addLocation(latDec,lngDec)
            print(newLoc)
            print(Location.objects.all().values())
        

    return HttpResponse("OK")
