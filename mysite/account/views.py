from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, UpdateView, DetailView

from account.forms import CustomUserCreationForm
from account.models import AnimeList, MangaList, CustomUser
from main_app.utils import DataMixin


class ProfileView(DataMixin, DetailView):
    template_name = "account/profile.html"
    model = CustomUser
    pk_url_kwarg = "id"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        c_def = super(ProfileView, self).get_user_context(title=self.request.user.username)
        return dict(list(context.items()) + list(c_def.items()))


class EditProfileView(DataMixin, UpdateView):
    template_name = "main_app/create_post_form.html"
    context_object_name = 'post'
    pk_url_kwarg = "id"
    form_class = CustomUserCreationForm
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        c_def = super(EditProfileView, self).get_user_context(title="Editing profile")
        return dict(list(context.items()) + list(c_def.items()))

    def get(self, request, *args, **kwargs):
        user_object = self.get_object()
        self.check_permission(request.user, user_object)
        return super(EditProfileView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_object = self.get_object()
        self.check_permission(request.user, user_object)
        return super(EditProfileView, self).post(request, *args, **kwargs)

    def check_permission(self, request_user, user_object):
        if request_user != user_object:
            raise PermissionDenied()


class ShowAnimeList(DataMixin, ListView):
    template_name = "account/list.html"
    model = AnimeList
    context_object_name = "list"

    def get_queryset(self):
        return AnimeList.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ShowAnimeList, self).get_context_data(**kwargs)
        choices = AnimeList.Status.choices
        lists = [context['list'].filter(status=choice[0]) for choice in choices]
        c_def = super(ShowAnimeList, self).get_user_context(title="Список аниме",
                                                            lists=lists,
                                                            choices=choices,
                                                            type="Anime")
        return dict(list(context.items()) + list(c_def.items()))


class ShowMangaList(DataMixin, ListView):
    template_name = "account/list.html"
    model = MangaList
    context_object_name = "list"

    def get_queryset(self):
        return MangaList.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ShowMangaList, self).get_context_data(**kwargs)
        choices = MangaList.Status.choices
        lists = [context['list'].filter(status=choice[0]) for choice in choices]
        c_def = super(ShowMangaList, self).get_user_context(title="Список манги",
                                                            lists=lists,
                                                            choices=choices,
                                                            type="Manga")
        return dict(list(context.items()) + list(c_def.items()))
