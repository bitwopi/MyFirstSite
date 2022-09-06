from rest_framework.response import Response
from rest_framework.decorators import api_view

from main_app.models import Anime, Character, Manga
from main_app.serializer import AnimeSerializer, CharacterSerializer, MangaSerializer


@api_view(["GET"])
def manga_api(request):
    instance = Manga.objects.filter(id=request.GET.get('id', 1))
    data = {}
    print(instance)
    if instance:
        data = MangaSerializer(instance[0]).data
        print(data)
    return Response(data)


@api_view(["GET"])
def character_api(request):
    instance = Character.objects.filter(id=request.GET.get('id', 293))
    data = {}
    print(instance)
    if instance:
        data = CharacterSerializer(instance[0]).data
        print(data)
    return Response(data)


@api_view(["GET"])
def anime_api(request):
    instance = Anime.objects.filter(id=request.GET.get('id', 87))
    data = {}
    print(instance)
    if instance:
        data = AnimeSerializer(instance[0]).data
        print(data)
    return Response(data)