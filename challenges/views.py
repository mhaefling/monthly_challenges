from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes a day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    
    return HttpResponse(challenge_text)

def monthly_challenges_by_number(request, month):
    month_text = None
    if month == 1:
        month_text = "January!"
    elif month == 2:
        month_text = "February!"
    elif month == 3:
        month_text = "March!"
    else:
        return HttpResponseNotFound("Invalid Month!")
    
    return HttpResponse(month_text)
