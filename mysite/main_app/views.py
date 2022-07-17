from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .forms import *

from .models import *

menu = ["About", "Create post", "Feedback", "Login"]

class MainAppHome(ListView):
    model = Anime
    template_name = 'main_app/index.html'
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Main page"
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/index.html'
