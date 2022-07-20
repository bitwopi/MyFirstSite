from django.contrib import admin
from .models import *
# Register your models here.


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'is_out', 'out_date',)
    search_fields = ('title', 'discription')
    list_editable = ('is_out',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Category, CategoryAdmin)
