from django.db import models
from django.urls import reverse


class Anime(models.Model):
    title = models.CharField(max_length=255)
    j_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name="Discription", null=True)
    rate = models.FloatField(verbose_name="Rating", null=True)
    is_out = models.BooleanField(default=False, verbose_name="Is out")
    out_date = models.DateField(verbose_name="Release date")
    cover = models.ImageField(upload_to="animes/covers", null=True, verbose_name="Cover")
    category = models.ManyToManyField('Category', verbose_name="Categories")
    type = models.ForeignKey('Type', verbose_name="Type", on_delete=models.PROTECT)
    episodes_now = models.IntegerField(verbose_name="Episodes now")
    episodes_all = models.IntegerField(verbose_name="Episodes all")
    duration = models.DurationField(verbose_name="Duration")
    studio = models.ForeignKey('Studio', on_delete=models.PROTECT, verbose_name="Studio")
    persons = models.ManyToManyField('Person', verbose_name="Authors")
    main_chars = models.ManyToManyField('Character', verbose_name="Main characters")
    source = models.ForeignKey('Manga', on_delete=models.PROTECT, null=True, verbose_name="Source")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'anime_slug': self.slug})

    def get_categories(self):
        result = []
        for cat in self.category.all():
            result.append(cat)
        return result

    def get_authors(self):
        result = []
        for a in self.persons.all():
            result.append(a)
        return result

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
    title = models.CharField(max_length=255)
    j_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name="Discription", null=True)
    rate = models.FloatField(verbose_name="Rating")
    release_date = models.DateField(verbose_name="Release date")
    cover = models.ImageField(upload_to="covers", null=True, verbose_name="Cover")
    category = models.ManyToManyField('Category', verbose_name="Categories")
    main_characters = models.ManyToManyField('Character', verbose_name="Characters")
    author = models.ForeignKey('Person', on_delete=models.PROTECT, verbose_name="Author")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'manga_slug': self.slug})

    def get_categories(self):
        result = []
        for cat in self.category.all():
            result.append(cat)
        return result

    def get_projects(self):
        return Anime.objects.filter(source__slug=self.slug)

    def get_main_chars(self):
        return self.main_characters.all()


class Character(models.Model):
    name = models.CharField(max_length=255)
    j_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name="Discription", null=True)
    voice_actor = models.ForeignKey('Person', on_delete=models.PROTECT, verbose_name="Voice actor")
    photo = models.ImageField(upload_to="characters/photos", null=True, verbose_name="Photo")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character', kwargs={'char_slug': self.slug})

    def get_projects(self):
        return list(Anime.objects.filter(main_chars__slug=self.slug)) \
               + list(Manga.objects.filter(main_characters__slug=self.slug))


class Career(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    j_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    birth_date = models.DateField(verbose_name="Birth date")
    career = models.ForeignKey('Career', on_delete=models.PROTECT, verbose_name="career")
    photo = models.ImageField(upload_to="persons/photos", null=True, verbose_name="Photo")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person', kwargs={'person_slug': self.slug})

    def get_projects(self):
        return list(Anime.objects.filter(main_chars__voice_actor__slug=self.slug)) \
               + list(Anime.objects.filter(persons__slug=self.slug))


class MPAA_rate(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(verbose_name="Discription", null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_manga_url(self):
        return reverse('category-manga', kwargs={'cat_slug': self.slug})

    def get_absolute_anime_url(self):
        return reverse('category-anime', kwargs={'cat_slug': self.slug})


class Studio(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    logo = models.ImageField(upload_to="studios/logos", null=True, verbose_name="Logo")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studio', kwargs={'st_slug': self.slug})