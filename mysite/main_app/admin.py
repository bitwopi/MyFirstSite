from django.contrib import admin
from .models import *
# Register your models here.


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'is_out', 'out_date', 'type',
                    'episodes_now', 'episodes_all', 'duration',)
    search_fields = ('title', 'description')
    list_editable = ('is_out', 'episodes_now')
    prepopulated_fields = {"slug": ("title",)}


class MangaAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ("title",)}


class CharacterAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


class PersonAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


class StudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Manga, MangaAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Career)
admin.site.register(MPAARate)
admin.site.register(Person, PersonAdmin)
