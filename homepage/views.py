from django.shortcuts import render

from homepage.models import Games

def index(request):
    games = Games.objects.all()
    return render(request, "homepage/index.html", {'games': games})