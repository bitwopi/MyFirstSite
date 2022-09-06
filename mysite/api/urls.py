from django.urls import path

from .views import anime_api, manga_api, character_api


urlpatterns = [
    path('anime/', anime_api, name="anime-api"),
    path('manga/', manga_api, name="manga-api"),
    path('character/', character_api, name="character-api"),
]
