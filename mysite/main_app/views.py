from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = ["About", "Create post", "Feedback", "Login"]

def index(request):
    posts = Anime.objects.all()
    return render(request, 'main_app/index.html', {"posts": posts, "menu": menu, 'title': "Main page"})
