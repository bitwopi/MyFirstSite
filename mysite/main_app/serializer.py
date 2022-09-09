from rest_framework import serializers
from .models import Anime, Manga, Character, Person, Studio, Category, Type


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
    type = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    main_characters = CharacterSerializer(many=True)
    author = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Manga
        fields = '__all__'

    def get_type(self, obj):
        return obj.type.name


class AnimeSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    main_chars = CharacterSerializer(many=True, read_only=True)
    persons = PersonSerializer(many=True, read_only=True)
    studios = StudioSerializer(many=True, read_only=True)
    source = MangaSerializer()

    class Meta:
        model = Anime
        fields = '__all__'

    def get_type(self, obj):
        return obj.type.name


