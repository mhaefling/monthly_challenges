from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes a day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Study for the CySA+ every day!",
    "may": "Ride your bike every day!",
    "june": "Its your birthday, take a break!",
    "july": "Work out for 2 hours a day!",
    "august": "Eat no meat for the entire month!",
    "september": "Take a 2 hour nap every day!",
    "october": "Prepare for Halloween!",
    "november": "Prepare for Thanksgiving!",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys())

    return HttpResponse(render(request, "challenges/index.html", {
        "month_list": months
    }))

def monthly_challenge(request, month):
    try:
        return HttpResponse(render(request,"challenges/challenge.html", {
            "text": monthly_challenges[month],
            "month": month
        }))
    except:
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    try:
        return HttpResponseRedirect(reverse("month-challenge", args=[months[month - 1]]))
    except:
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")