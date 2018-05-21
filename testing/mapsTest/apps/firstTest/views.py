from django.shortcuts import redirect, render, HttpResponse

def index(request):

    return render(request, 'firstTest/index.html')



def embed(request):

    return render(request, 'firstTest/embedded.html')