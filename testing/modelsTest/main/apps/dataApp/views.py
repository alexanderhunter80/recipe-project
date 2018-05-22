from django.shortcuts import render, HttpResponse

def index(request):
    response = "testing"
    return HttpResponse(response)
