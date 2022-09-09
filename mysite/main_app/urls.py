from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', MainAppHome.as_view(), name="home"),
    path('login/', LoginUser.as_view(), name="login"),
    path('registration/', RegisterUser.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('create/', CreatePost.as_view(), name="create"),
    path('post/anime/<slug:anime_slug>/', ShowPostAnime.as_view(), name='post'),
    path('post/manga/<slug:manga_slug>/', ShowPostManga.as_view(), name='post'),
    path('post/anime/<slug:anime_slug>/edit/', EditPostAnime.as_view(), name="edit-anime"),
    path('post/manga/<slug:manga_slug>/edit/', EditPostManga.as_view(), name="edit-manga"),
    path('post/character/<slug:char_slug>/edit/', EditPostCharacter.as_view(), name="edit-character"),
    path('post/person/<slug:person_slug>/edit/', EditPostPerson.as_view(), name="edit-person"),
    path('category/anime/<slug:cat_slug>/', ShowAnimeCategory.as_view(), name="category-anime"),
    path('category/manga/<slug:cat_slug>/', ShowMangaCategory.as_view(), name="category-manga"),
    path('studio/<slug:st_slug>/', ShowStudio.as_view(), name="studio"),
    path('person/<slug:person_slug>/', ShowPostPerson.as_view(), name="person"),
    path('character/<slug:char_slug>/', ShowPostCharacter.as_view(), name="character"),
    path('reset_password', ResetPassword.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="main_app/registration/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name="main_app/registration/reset_password_complete.html"), name="password_reset_complete"),
]
