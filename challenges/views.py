from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challengeText = None
    if month == "january":
        challengeText = "En Enero hay que comer vegano una vez al dia"
    elif month == "february":
        challengeText = "En Febrero hay que caminar 20 minutos todos los dias!"
    elif month == 'march':
        challengeText = "En Marzo hay que tomar agua cada 2 horas!"
    else:
        return HttpResponseNotFound("Esto no es un mes")
    return HttpResponse(challengeText)
