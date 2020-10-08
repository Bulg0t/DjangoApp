from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Witaj w Django")

def onas(request):
    return HttpResponse("<h1>Informacje o nas</h1>")