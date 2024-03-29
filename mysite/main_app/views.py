import os

import dotenv
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.db.models import Q, Avg
from django.core.exceptions import PermissionDenied
from rest_framework import generics

from .forms import *
from .models import *
from .serializer import AnimeSerializer, MangaSerializer, CharacterSerializer, PersonSerializer, StudioSerializer, \
    AnimeListSerializer, MangaListSerializer
from .utils import *

dotenv.load_dotenv()
PAGINATE_NUMBER = int(os.getenv('POST_NUMBER_IN_PAGE', 10))


# ---Class views---
class ShowCatalog(DataMixin, ListView):
    paginate_by = PAGINATE_NUMBER
    template_name = 'main_app/lists/index.html'
    context_object_name = 'posts'
    form = FilterAnimeForm()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowCatalog, self).get_context_data(**kwargs)
        c_def = super(ShowCatalog, self).get_user_context(title="YourAnimeList", form=self.form)
        for filt in super(ShowCatalog, self).filters:
            if filt in self.request.GET:
                context[filt] = self.request.GET[filt]
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        queryset = self.model.objects.all()
        if 'type' in self.request.GET:
            if self.request.GET['type'] != '':
                print(self.request.GET.get('type'))
                queryset = queryset.filter(type=self.request.GET['type'])
        if 'rate' in self.request.GET:
            if self.request.GET['rate'] != '':
                rate_filter = float(self.request.GET['rate'])
                if self.model == Anime:
                    queryset = queryset.annotate(avg_rate=Avg('animelist__rate')).filter(Q(avg_rate__gte=rate_filter))
                else:
                    queryset = queryset.annotate(avg_rate=Avg('mangalist__rate')).filter(Q(avg_rate__gte=rate_filter))
        if 'category' in self.request.GET:
            if self.request.GET['category'] != '':
                queryset = queryset.filter(category=self.request.GET['category'])
        if 'studios' in self.request.GET:
            if self.request.GET['studios'] != '':
                queryset = queryset.filter(studios=self.request.GET['studios'])
        return queryset


class ShowAnimeCatalogView(ShowCatalog):
    model = Anime


class ShowMangaCatalogView(ShowCatalog):
    model = Manga
    form = FilterMangaForm()


# Login views
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/registration/registration_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        c_def = super(RegisterUser, self).get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'main_app/registration/login_form.html'
    context_object_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        c_def = super(LoginUser, self).get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


# Create views
class CreatePost(DataMixin, CreateView):
    form_class = CreatePostFormAnime
    template_name = "main_app/create_post_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        c_def = super(CreatePost, self).get_user_context(title="Create post", button_title="Add")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


# Show views
class ShowPostAnime(DataMixin, DetailView):
    model = Anime
    context_object_name = 'post'
    template_name = 'main_app/posts/post_anime.html'
    slug_url_kwarg = 'anime_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostAnime, self).get_context_data(**kwargs)
        try:
            anime_list = AnimeList.objects.filter(user=self.request.user.id).get(anime=context['post'].id)
        except:
            anime_list = None
        c_def = super(ShowPostAnime, self).get_user_context(title=context['post'],
                                                            type="anime",
                                                            manga_types=[7, 8, 9, 11],
                                                            list=anime_list,
                                                            status=AnimeList.Status)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostManga(DataMixin, DetailView):
    model = Manga
    context_object_name = 'post'
    template_name = 'main_app/posts/post_manga.html'
    slug_url_kwarg = 'manga_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostManga, self).get_context_data(**kwargs)
        try:
            manga_list = MangaList.objects.filter(user=self.request.user.id).get(manga=context['post'].id)
        except:
            manga_list = None
        c_def = super(ShowPostManga, self).get_user_context(title=context['post'],
                                                            type="manga",
                                                            list=manga_list,
                                                            status=MangaList.Status)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostPerson(DataMixin, DetailView):
    model = Person
    context_object_name = 'post'
    template_name = 'main_app/posts/post_character.html'
    slug_url_kwarg = 'person_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostPerson, self).get_context_data(**kwargs)
        c_def = super(ShowPostPerson, self).get_user_context(title=context['post'],
                                                             type="person",
                                                             manga_types=[7, 8, 9, 11],)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPostCharacter(DataMixin, DetailView):
    model = Character
    context_object_name = 'post'
    template_name = 'main_app/posts/post_character.html'
    slug_url_kwarg = 'char_slug'

    def get_context_data(self, **kwargs):
        context = super(ShowPostCharacter, self).get_context_data(**kwargs)
        c_def = super(ShowPostCharacter, self).get_user_context(title=context['post'],
                                                                type="character",
                                                                manga_types=[7, 8, 9, 11],)
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
        return Anime.objects.filter(studios__slug=self.kwargs['st_slug'])

    def get_studio(self):
        return Studio.objects.filter(slug=self.kwargs['st_slug'])


# Edit views
class EditPost(DataMixin, UpdateView):
    """ Base class for post edit """
    template_name = "main_app/create_post_form.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        return super(EditPost, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        self.check_permission(request.user)
        return super(EditPost, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.check_permission(request.user)
        return super(EditPost, self).post(request, *args, **kwargs)

    def check_permission(self, user):
        if user.is_staff is False:
            raise PermissionDenied()


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


# Reset views
class ResetPassword(DataMixin, auth_views.PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'main_app/registration/reset_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super(ResetPassword, self).get_context_data(**kwargs)
        c_def = super(ResetPassword, self).get_user_context(title="Восстановление пароля")
        return dict(list(context.items()) + list(c_def.items()))


class ResetPasswordConfirm(auth_views.PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name = 'main_app/registration/reset_form.html'
    context_object_name = 'regs'
    success_url = reverse_lazy('password_reset_complete')


# ---API views---
# Detail
class AnimeDetailAPIView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    lookup_field = 'slug'


class MangaDetailAPIView(generics.RetrieveAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'slug'


class CharacterDetailAPIView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'slug'


class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'slug'


class StudioDetailAPIView(generics.RetrieveAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    lookup_field = 'slug'


# List
class AnimeListAPIView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class MangaListAPIView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer


class CharacterListAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class PersonListAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class StudioListAPIView(generics.ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class AnimeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AnimeListSerializer

    def get_queryset(self):
        queryset = AnimeList.objects.all()
        if self.request.GET:
            if "status" in self.request.GET:
                queryset = queryset.filter(status=self.request.GET["status"])
            if "user" in self.request.GET:
                queryset = queryset.filter(user=self.request.GET["user"])
        return queryset


class AnimeListUpdateAPIView(generics.UpdateAPIView):
    queryset = AnimeList.objects.all()
    serializer_class = AnimeListSerializer


class MangaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MangaListSerializer

    def get_queryset(self):
        queryset = MangaList.objects.all()
        if self.request.GET:
            if "status" in self.request.GET:
                queryset = queryset.filter(status=self.request.GET["status"])
            if "user" in self.request.GET:
                queryset = queryset.filter(user=self.request.GET["user"])
        return queryset


class MangaListUpdateAPIView(generics.UpdateAPIView):
    queryset = MangaList.objects.all()
    serializer_class = MangaListSerializer


# ---Function based views---
def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        q = request.GET['q']
        multiple_q_titles = Q(Q(title__icontains=q) | Q(synonyms__icontains=q))
        multiple_q_names = Q(Q(name__icontains=q) | Q(synonyms__icontains=q))
        context_a = Anime.objects.filter(multiple_q_titles)
        context_m = Manga.objects.filter(multiple_q_titles)
        context_c = Character.objects.filter(multiple_q_names)
        context_p = Person.objects.filter(multiple_q_names)
        context = {
            'data': list(context_a) + list(context_m) + list(context_p) + list(context_c),
            'menu': menu
        }
        print(context)
        return render(request=request, context=context, template_name='main_app/lists/search_list.html')


def logout_user(request):
    logout(request)
    return redirect('login')
