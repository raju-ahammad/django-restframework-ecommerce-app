from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render


def home(request):
    return JsonResponse({'info': 'django course ', "name": "Raju"})

def homePage(request):
    html = "<h1>This page have nothing</h1>"
    return HttpResponse(html)
    