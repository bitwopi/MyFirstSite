import os

import dotenv
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .forms import *
from .models import *
from .utils import *

dotenv.load_dotenv()
PAGINATE_NUMBER = int(os.getenv('POSTS_NUMBER_IN_PAGE', 10))


class MainAppHome(DataMixin, ListView):
    paginate_by = PAGINATE_NUMBER
    model = Anime
    template_name = 'main_app/lists/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainAppHome, self).get_context_data(**kwargs)
        c_def = super(MainAppHome, self).get_user_context(title="YourAnimeList")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/registration/registration_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        c_def = super(RegisterUser, self).get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'main_app/registration/login_form.html'
    context_object_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class CreatePost(DataMixin, CreateView):
    form_class = CreatePostFormAnime
    template_name = "main_app/create_post_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        c_def = super(CreatePost, self).get_user_context(title="Create post", button_title="Add")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class ShowPostAnime(DataMixin, DetailView):
    model = Anime
    context_object_name = 'post'
    template_name = 'main_app/posts/post_anime.html'
    slug_url_kwarg = 'anime_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostAnime, self).get_context_data(**kwargs)
        c_def = super(ShowPostAnime, self).get_user_context(title=context['post'], type="anime")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostManga(DataMixin, DetailView):
    model = Manga
    context_object_name = 'post'
    template_name = 'main_app/posts/post_manga.html'
    slug_url_kwarg = 'manga_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostManga, self).get_context_data(**kwargs)
        c_def = super(ShowPostManga, self).get_user_context(title=context['post'], type="manga")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostPerson(DataMixin, DetailView):
    model = Person
    context_object_name = 'post'
    template_name = 'main_app/posts/post_character.html'
    slug_url_kwarg = 'person_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostPerson, self).get_context_data(**kwargs)
        c_def = super(ShowPostPerson, self).get_user_context(title=context['post'], type="person")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostCharacter(DataMixin, DetailView):
    model = Character
    context_object_name = 'post'
    template_name = 'main_app/posts/post_character.html'
    slug_url_kwarg = 'char_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostCharacter, self).get_context_data(**kwargs)
        c_def = super(ShowPostCharacter, self).get_user_context(title=context['post'], type="character")
        return dict(list(context.items()) + list(c_def.items()))


class EditPost(DataMixin, UpdateView):
    """ Base class for post edit """
    template_name = "main_app/create_post_form.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        return super(EditPost, self).get_context_data(**kwargs)


class EditPostAnime(EditPost):
    form_class = CreatePostFormAnime
    model = Anime
    slug_url_kwarg = 'anime_slug'

    def get_context_data(self, **kwargs):
        context = super(EditPostAnime, self).get_context_data(**kwargs)
        c_def = super(EditPostAnime, self).get_user_context(title=f"Editing post: {context['post']}")
        return dict(list(context.items()) + list(c_def.items()))


class EditPostCharacter(EditPost):
    form_class = CreatePostFormCharacter
    model = Character
    slug_url_kwarg = 'char_slug'

    def get_context_data(self, **kwargs):
        context = super(EditPostCharacter, self).get_context_data(**kwargs)
        c_def = super(EditPostCharacter, self).get_user_context(title=f"Editing post: {context['post']}")
        return dict(list(context.items()) + list(c_def.items()))


class EditPostPerson(EditPost):
    form_class = CreatePostFormPerson
    model = Person
    slug_url_kwarg = 'person_slug'

    def get_context_data(self, **kwargs):
        context = super(EditPostPerson, self).get_context_data(**kwargs)
        c_def = super(EditPostPerson, self).get_user_context(title=f"Editing post: {context['post']}")
        return dict(list(context.items()) + list(c_def.items()))


class EditPostManga(EditPost):
    form_class = CreatePostFormManga
    model = Manga
    slug_url_kwarg = 'manga_slug'

    def get_context_data(self, **kwargs):
        context = super(EditPostManga, self).get_context_data(**kwargs)
        c_def = super(EditPostManga, self).get_user_context(title=f"Editing post: {context['post']}")
        return dict(list(context.items()) + list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    """ Base class for category items output """
    paginate_by = PAGINATE_NUMBER
    template_name = "main_app/lists/category_list.html"
    context_object_name = 'posts'
    slug_url_kwarg = 'cat_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowCategory, self).get_context_data(**kwargs)
        c_def = super(ShowCategory, self).get_user_context(title="YourAnimeList", name=self.get_category()[0].name)
        return dict(list(context.items()) + list(c_def.items()))

    def get_category(self):
        return Category.objects.filter(slug=self.kwargs['cat_slug'])


class ShowAnimeCategory(ShowCategory):
    model = Anime

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowAnimeCategory, self).get_context_data(**kwargs)
        c_def = super(ShowAnimeCategory, self).get_user_context(type="Anime")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Anime.objects.filter(category__slug=self.kwargs['cat_slug'])


class ShowMangaCategory(ShowCategory):
    model = Manga

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowMangaCategory, self).get_context_data(**kwargs)
        c_def = super(ShowMangaCategory, self).get_user_context(type="Manga")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Manga.objects.filter(category__slug=self.kwargs['cat_slug'])


class ShowStudio(DataMixin, ListView):
    paginate_by = PAGINATE_NUMBER
    model = Anime
    template_name = "main_app/lists/studio_list.html"
    context_object_name = 'posts'
    slug_url_kwarg = 'st_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowStudio, self).get_context_data(**kwargs)
        c_def = super(ShowStudio, self).get_user_context(title="YourAnimeList", name=self.get_studio()[0].name)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Anime.objects.filter(studio__slug=self.kwargs['st_slug'])

    def get_studio(self):
        return Studio.objects.filter(slug=self.kwargs['st_slug'])


class ResetPassword(auth_views.PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'main_app/registration/reset_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('password_reset_done')


class ResetPasswordConfirm(auth_views.PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name = 'main_app/registration/reset_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('password_reset_complete')


def logout_user(request):
    logout(request)
    return redirect('login')
