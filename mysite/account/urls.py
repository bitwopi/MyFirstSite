from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("anime_list/", ShowAnimeList.as_view(), name="anime_list"),
]
