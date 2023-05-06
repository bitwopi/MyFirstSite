from django.urls import path

from main_app.views import AnimeDetailAPIView, MangaDetailAPIView, CharacterDetailAPIView, PersonDetailAPIView, \
    StudioDetailAPIView, AnimeListAPIView, MangaListAPIView, CharacterListAPIView, PersonListAPIView, \
    StudioListAPIView, AnimeListCreateAPIView, AnimeListUpdateAPIView, MangaListCreateAPIView, MangaListUpdateAPIView

urlpatterns = [
    path('anime/', AnimeListAPIView.as_view(), name='api-anime'),
    path('manga/', MangaListAPIView.as_view(), name='api-manga'),
    path('character/', CharacterListAPIView.as_view(), name='api-character'),
    path('person/', PersonListAPIView.as_view(), name='api-person'),
    path('studio/', StudioListAPIView.as_view(), name='api-studio'),
    path('anime/<slug:slug>/', AnimeDetailAPIView.as_view(), name='api-anime-detail'),
    path('manga/<slug:slug>/', MangaDetailAPIView.as_view(), name='api-manga-detail'),
    path('character/<slug:slug>/', CharacterDetailAPIView.as_view(), name='api-character-detail'),
    path('person/<slug:slug>/', PersonDetailAPIView.as_view(), name='api-person-detail'),
    path('studio/<slug:slug>/', StudioDetailAPIView.as_view(), name='api-studio-detail'),
    path('animelist/', AnimeListCreateAPIView.as_view(), name='api-animelist'),
    path('animelist/<int:pk>', AnimeListUpdateAPIView.as_view(), name='api-animelist-detail'),
    path('mangalist/', MangaListCreateAPIView.as_view(), name='api-mangalist'),
    path('mangalist/<int:pk>', MangaListUpdateAPIView.as_view(), name='api-mangalist-detail'),
]