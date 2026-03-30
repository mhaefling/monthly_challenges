from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("Eath no meat for the entire month!")

def februrary(request):
    return HttpResponse("Walk for at least 20 mins a day!")