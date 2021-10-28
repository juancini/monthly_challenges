from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

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
    "october": "En Octubre hay que ver una peli de miedo todos los dias",
    "november": "En Noviembre hay que celebrar mi cumple todos los dias",
    "december": "En Diciembre hay que hacer un regalo todos los dias"
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    # check si el mes es mayor a la cantida de meses
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    forward_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challengeText = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challengeText,
            "month": month
        })
    except:
        return HttpResponseNotFound('Mes sin soporte')
