from django.db import models
from django.urls import reverse


class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name="Discription")
    rate = models.FloatField(verbose_name="Rating")
    is_out = models.BooleanField(default=False, verbose_name="Is out")
    out_date = models.DateField(auto_now_add=True, verbose_name="Release date")
    cover = models.ImageField(upload_to="covers", null=True, verbose_name="Cover")
    category = models.ManyToManyField('Category', verbose_name="Categories")
    type = models.ForeignKey('Type', verbose_name="Type", on_delete=models.PROTECT)
    episodes_now = models.IntegerField(verbose_name="Episodes now")
    episodes_all = models.IntegerField(verbose_name="Episodes all")
    duration = models.DurationField(verbose_name="Duration")
    studio = models.ForeignKey('Studio', on_delete=models.PROTECT, verbose_name="Studio")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def get_categories(self):
        result = []
        for cat in self.category.all():
            result.append(cat)
        return result

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

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


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