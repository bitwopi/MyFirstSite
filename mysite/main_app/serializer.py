from rest_framework import serializers
from .models import Anime, Manga, Character, Person, Studio, Category
from account.models import AnimeList, MangaList


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    career = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Person
        fields = '__all__'

    def get_career(self, obj):
        return obj.career.name


class CharacterSerializer(serializers.ModelSerializer):
    voice_actor = PersonSerializer(read_only=True)

    class Meta:
        model = Character
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(
        view_name='api-manga-detail',
        lookup_field='slug'
    )
    type = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    main_characters = CharacterSerializer(many=True)
    author = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Manga
        fields = [
            "api_url",
            "id",
            "title",
            "synonyms",
            "slug",
            "description",
            "rate",
            "release_date",
            "cover",
            "type",
            "category",
            "main_characters",
            "author",
        ]

    def get_type(self, obj):
        return obj.type.name


class AnimeSerializer(serializers.ModelSerializer):
    api_url = serializers.HyperlinkedIdentityField(
        view_name='api-anime-detail',
        lookup_field='slug'
    )
    type = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    main_chars = CharacterSerializer(many=True, read_only=True)
    persons = PersonSerializer(many=True, read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    source = MangaSerializer()

    class Meta:
        model = Anime
        fields = [
            "api_url",
            "id",
            "type",
            "category",
            "main_chars",
            "persons",
            "studios",
            "source",
            "title",
            "synonyms",
            "slug",
            "description",
            "rate",
            "is_out",
            "out_date",
            "cover",
            "episodes_now",
            "episodes_all",
            "duration",
        ]

    def get_type(self, obj):
        return obj.type.name


class AnimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeList
        fields = '__all__'


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaList
        fields = '__all__'
