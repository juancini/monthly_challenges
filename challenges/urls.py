from django.urls import path

from . import views

urlpatterns = [
    #En estos casos, el orden importa, si la 7 y 8 estuvieran al reves,
    #pasaria siempre a monthly_challenge
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
