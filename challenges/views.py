from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


monthly_challenges = {
    "january": "En Enero hay que comer vegano una vez al dia",
    "february": "En Febrero hay que caminar 20 minutos todos los dias!",
    "march": "En Marzo hay que tomar agua cada 2 horas!",
    "april": "En Abril hay que hacer un chiste todos los dias!",
    "may": "En Mayo hay que ordenar la pieza los martes y jueves!",
    "june": "En Junio hay que aprender algo nuevo todos los dias!",
    "july": "En Julio hay que comer frutas todos los dias",
    "august": "En Agosto hay que meditar media hora todos los dias!",
    "september": "En Septiembre hay que poner September 24/7",
    "November": "En Noviembre hay que celebrar mi cumple todos los dias",
    "December": "En Diciembre hay que hacer un regalo todos los dias"
}

def monthly_challenge_by_number(request, month):
    months  = list(monthly_challenges.keys())
    forward_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
    try:
        challengeText = monthly_challenges[month]
    except:
        return HttpResponseNotFound('Mes sin soporte')
    return HttpResponse(challengeText)
