from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse
# from main_app.models import Anime, Manga


# USER MODEL EXTENSION
class CustomUser(AbstractUser):
    # DATABASE FIELDS
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name="Avatar")
    anime_list = models.ManyToManyField("main_app.Anime", verbose_name="Animes", through="AnimeList")
    manga_list = models.ManyToManyField("main_app.Manga", verbose_name="Mangas", through="MangaList")
    # MANAGER TO CREATE USERS
    objects = UserManager()

    # META CLASS
    class Meta:
        ordering = ['username']

    # TO STRING METHOD
    def __str__(self):
        return self.username

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('profile', kwargs={'id': self.pk})


class AnimeList(models.Model):
    class Meta:
        unique_together = (("anime", "user"),)

    class Status(models.IntegerChoices):
        VIEWED = 1, "Просмотрено"
        WATCHING = 2, "Смотрю"
        PLANNED = 3, "Запланировано"
        POSTPONED = 4, "Отложено"
        DROPPED = 5, "Брошено"

    anime = models.ForeignKey("main_app.Anime", on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PLANNED)
    rate = models.PositiveSmallIntegerField(verbose_name="Rating", null=True, default=None)


class MangaList(models.Model):
    class Meta:
        unique_together = (("manga", "user"),)

    class Status(models.IntegerChoices):
        READ = 1, "Просмотрено"
        READING = 2, "Смотрю"
        PLANNED = 3, "Запланировано"
        POSTPONED = 4, "Отложено"
        DROPPED = 5, "Брошено"

    manga = models.ForeignKey("main_app.Manga", on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.PLANNED)
    rate = models.PositiveSmallIntegerField(verbose_name="Rating", null=True, default=None)
