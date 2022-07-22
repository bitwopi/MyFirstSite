from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.detail import BaseDetailView

from .forms import *

from .models import *
from .utils import *


class MainAppHome(DataMixin, ListView):
    model = Anime
    template_name = 'main_app/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainAppHome, self).get_context_data(**kwargs)
        c_def = super(MainAppHome, self).get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/registration_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        c_def = super(RegisterUser, self).get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'main_app/login_form.html'
    context_object_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class CreatePost(DataMixin, CreateView):
    form_class = CreatePostForm
    template_name = "main_app/create_post_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        c_def = super(CreatePost, self).get_user_context(title="Create post", button_title="Add")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class ShowPost(DataMixin, DetailView):
    model = Anime
    context_object_name = 'post'
    template_name = 'main_app/post.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPost, self).get_context_data(**kwargs)
        c_def = super(ShowPost, self).get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class EditPost(DataMixin, UpdateView):
    model = Anime
    form_class = CreatePostForm
    template_name = "main_app/create_post_form.html"
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(EditPost, self).get_context_data(**kwargs)
        c_def = super(EditPost, self).get_user_context(title="Editing post")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
