from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# USER MODEL EXTENSION
class CustomUser(AbstractUser):
    # DATABASE FIELDS
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name="Avatar")


class Anime(models.Model):
    # DATABASE FIELDS
    title = models.CharField(max_length=255)
    synonyms = models.TextField()
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name="Description", blank=True)
    rate = models.FloatField(verbose_name="Rating", default=0)
    is_out = models.BooleanField(default=False, verbose_name="Is out")
    out_date = models.DateField(verbose_name="Release date", null=True, blank=True)
    cover = models.ImageField(upload_to="animes/covers", null=True, verbose_name="Cover", blank=True)
    category = models.ManyToManyField('Category', verbose_name="Categories")
    type = models.ForeignKey('Type', verbose_name="Type", on_delete=models.PROTECT)
    episodes_now = models.IntegerField(verbose_name="Episodes now", default=0)
    episodes_all = models.IntegerField(verbose_name="Episodes all", null=True, default=0)
    duration = models.DurationField(verbose_name="Duration", null=True, default=0)
    studios = models.ManyToManyField('Studio', verbose_name="Studios")
    persons = models.ManyToManyField('Person', verbose_name="Authors", blank=True)
    main_chars = models.ManyToManyField('Character', verbose_name="Main characters")
    source = models.ForeignKey('Manga', on_delete=models.SET_NULL, null=True, verbose_name="Source", blank=True)

    # META CLASS
    class Meta:
        ordering = ['title']

    # TO STRING METHOD
    def __str__(self):
        return self.title

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('post', kwargs={'anime_slug': self.slug})

    # OTHER METHODS
    def get_categories(self):
        return [cat for cat in self.category.all()]

    def get_authors(self):
        return self.persons.all()

    def get_studios(self):
        return self.studios.all()

    def get_main_chars(self):
        return self.main_chars.all()

    def get_status(self):
        if self.is_out:
            status = "Release"
        elif self.episodes_now > 0:
            status = "Ongoing"
        else:
            status = "Announcement"
        return status

    def get_minutes(self):
        return int(self.duration.seconds / 60)

    def get_hours(self):
        return int(self.duration.seconds / 3600)


class Manga(models.Model):
    # DATABASE FIELDS
    title = models.CharField(max_length=255)
    synonyms = models.TextField()
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name="Description", blank=True)
    rate = models.FloatField(verbose_name="Rating", null=True)
    release_date = models.DateField(verbose_name="Release date", null=True)
    cover = models.ImageField(upload_to="manga/covers", null=True, verbose_name="Cover")
    category = models.ManyToManyField('Category', verbose_name="Categories")
    main_characters = models.ManyToManyField('Character', verbose_name="Characters")
    author = models.ManyToManyField('Person', verbose_name="Authors")
    type = models.ForeignKey('Type', verbose_name="Type", on_delete=models.SET_NULL, null=True)

    # META CLASS
    class Meta:
        ordering = ['title']

    # TO STRING METHOD
    def __str__(self):
        return self.title

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('post', kwargs={'manga_slug': self.slug})

    # OTHER METHODS
    def get_categories(self):
        return [cat for cat in self.category.all()]

    def get_projects(self):
        return Anime.objects.filter(source__slug=self.slug)

    def get_main_chars(self):
        return self.main_characters.all()


class Character(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=255)
    synonyms = models.TextField()
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    description = models.TextField(verbose_name="Description", blank=True)
    voice_actor = models.ForeignKey('Person', null=True, on_delete=models.PROTECT, verbose_name="Voice actor")
    photo = models.ImageField(upload_to="character/photos", null=True, verbose_name="Photo")

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('character', kwargs={'char_slug': self.slug})

    # OTHER METHODS
    def get_projects(self):
        return list(Anime.objects.filter(main_chars__slug=self.slug)) \
               + list(Manga.objects.filter(main_characters__slug=self.slug))


class Career(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=255)

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name


class Person(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=255)
    synonyms = models.TextField()
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    birth_date = models.DateField(verbose_name="Birth date", null=True)
    career = models.ManyToManyField('Career', verbose_name="Career")
    photo = models.ImageField(upload_to="persons/photos", null=True, verbose_name="Photo")

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('person', kwargs={'person_slug': self.slug})

    # OTHER METHODS
    def get_projects(self):
        return list(Anime.objects.filter(main_chars__voice_actor__slug=self.slug)) \
               + list(Anime.objects.filter(persons__slug=self.slug))


class MPAARate(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=50)
    description = models.TextField(verbose_name="Description", blank=True)

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name


class Type(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=50)

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name


class Category(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # ABSOLUTE URL METHODS
    def get_absolute_manga_url(self):
        return reverse('category-manga', kwargs={'cat_slug': self.slug})

    def get_absolute_anime_url(self):
        return reverse('category-anime', kwargs={'cat_slug': self.slug})


class Studio(models.Model):
    # DATABASE FIELDS
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    logo = models.ImageField(upload_to="studios/logos", null=True, verbose_name="Logo")

    # META CLASS
    class Meta:
        ordering = ['name']

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('studio', kwargs={'st_slug': self.slug})
